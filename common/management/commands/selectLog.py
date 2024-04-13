import pandas as pd
import pickle
from django.core.management.base import BaseCommand
from django.db import transaction
from Existing_db import models
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer
from django.utils import timezone
from datetime import timedelta, datetime, time
from time import time as timecheck
import logging

logger = logging.getLogger('django')


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        try:
            logger.info("Start Set Recommend")
            today = timezone.now().date()
            start_of_yesterday = datetime.combine(today, time.min).replace(tzinfo=timezone.utc)
            end_of_yesterday = datetime.combine(today, time.max).replace(tzinfo=timezone.utc)
            users = models.UserAccount.objects.filter(last_login__range=(start_of_yesterday, end_of_yesterday))
            recommends = models.Recommend.objects.filter(created_who__in=users)
            to_update = []
            products = pickle.load(open('common/product.pickle', 'rb'))
            cosine_sim = pickle.load(open('common/cosine_sim.pickle', 'rb'))
            for user in users:
                logger.info("Today Login User {}".format(user.user_id))
                try:
                    reco = recommends.get(created_who=user.user_id)
                except models.Recommend.DoesNotExist:
                    # Recommend 객체가 없는 경우 새로운 객체 생성
                    reco = models.Recommend(created_who=user, product_list="")
                categories = []
                logs = models.UserLog.objects.filter(created_who=user.user_id)
                for log in logs:
                    if log.product_id is None:
                        continue
                    product = models.Product.objects.get(product_id=log.product_id)
                    categories.append(product.pd_category)
                category_str = ",".join(categories)

                indices = pd.Series(products.index, index=products['product_id']).drop_duplicates()

                recommended_products = get_recommend(category_str, products, cosine_sim, indices)
                recommended_str = ",".join([str(product) for product in recommended_products])
                reco.product_list = recommended_str
                to_update.append(reco)
            models.Recommend.objects.bulk_update(to_update, ['product_list'])
            self.stdout.write(self.style.SUCCESS('Successfully'))
            logger.info("SET User recommend Successfully")
        except Exception as e:
            error_message = f"Failed to set User recommend. Error: {str(e)}"
            self.stdout.write(self.style.ERROR(error_message))
            logger.error(error_message)


def get_recommend(category, products, consine_sim, indices):
    # category에 기반하여 벡터화
    tfidf = CountVectorizer()
    tfidf_matrix = tfidf.fit_transform(products['pd_category'])

    # 입력된 category도 같은 vectorizer를 활용해 변환
    category_vector = tfidf.transform([category])

    # 입력된 category와 모든 products 간의 코사인 유사도 계산
    consine_sim = linear_kernel(category_vector, tfidf_matrix)

    # 유사도를 기준으로 상위 10개 products를 추천
    sim_scores = list(enumerate(consine_sim[0]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:31]

    product_indices = [i[0] for i in sim_scores]

    return products['product_id'].iloc[product_indices]
