from collections import Counter

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
        product_pickes = pickle.load(open('common/product.pickle', 'rb'))
        # category에 기반하여 벡터화
        tfidf = CountVectorizer()
        tfidf_matrix = tfidf.fit_transform(product_pickes['product_category'])
        try:
            logger.info("Start Set Recommend")
            today = timezone.now().date()
            start_of_yesterday = datetime.combine(today, time.min).replace(tzinfo=timezone.utc)
            end_of_yesterday = datetime.combine(today, time.max).replace(tzinfo=timezone.utc)
            users = models.UserAccount.objects.filter(last_login__range=(start_of_yesterday, end_of_yesterday))
            users = models.UserInfo.objects.filter(user_id__in=users)
            recommends = {reco.created_who_id: reco for reco in models.Recommend.objects.filter(created_who__in=users)}
            to_update = []
            to_create = []
            for user in users:
                logger.info("Today Login User {}".format(user.user_id))
                reco = recommends.get(user.user_id)
                if reco is None:
                    print(user.user_id, "  is None")
                    # Recommend 객체가 없는 경우 새로운 객체 생성
                    create_reco = models.Recommend(created_who=user, product_list="")
                    to_create.append(create_reco)
                    continue
                # None이 아닌 모든 product_id를 추출한다.
                product_ids = list(models.UserLog.objects.filter(created_who=user.user_id).exclude(
                    # 필터링 된 결과에서 product_id 필드 값을 리스트 형태로 추출한다.
                    # flat옵션을 통해 결과를 하나의 List로 평탄화하여 반환한다. True가 없다면 튜플들의 리스트 형태로 반환된다.
                    product_id=None).values_list('product_id', flat=True))[:20]
                products = models.Product.objects.filter(product_id__in=product_ids)
                categories = [product.product_category for product in products]
                category_str = ",".join(categories)
                category_count = Counter(categories)
                print(user.user_id)
                print(category_count)

                recommended_products = get_recommend(category_str, product_pickes, tfidf, tfidf_matrix)
                recommended_str = ",".join([str(product) for product in recommended_products])
                if recommended_products is None:
                    print(user.user_id)
                reco.product_list = recommended_str
                to_update.append(reco)
            print("created is Not OK")
            models.Recommend.objects.bulk_create(to_create)
            print("created is OK")
            models.Recommend.objects.bulk_update(to_update, ['product_list'])
            self.stdout.write(self.style.SUCCESS('Successfully'))
            logger.info("SET User recommend Successfully")
        except Exception as e:
            error_message = f"Failed to set User recommend. Error: {str(e)}"
            self.stdout.write(self.style.ERROR(error_message))
            logger.error(error_message)


def get_recommend(category, products, tfidf, tfidf_matrix):
    # 입력된 category도 같은 vectorizer를 활용해 변환
    category_vector = tfidf.transform([category])

    # 입력된 category와 모든 products 간의 코사인 유사도 계산
    consine_sim = linear_kernel(category_vector, tfidf_matrix)

    # 유사도를 기준으로 상위 30개 products를 추천
    sim_scores = list(enumerate(consine_sim[0]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[:30]

    product_indices = [i[0] for i in sim_scores]

    return products['product_id'].iloc[product_indices]
