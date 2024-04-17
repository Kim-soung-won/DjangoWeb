import random
from django.db import transaction
from Existing_db import models
from django.core.management.base import BaseCommand

from common.SettingDummyData.RandomDateTime import random_datetime


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        products = models.Product.objects.all()
        to_create_user_log = []
        to_create_love = []
        to_update_count_love = []

        # 중복 체크를 위한 set
        existing_combinations = set()

        for i in range(100000):
            print(i)
            rand: int = random.randint(1, 5000)
            user = models.UserInfo.objects.get(user_id=rand)
            rand: int = random.randint(0, 100)
            product = products[rand]
            love_exists = models.Love.objects.filter(created_who=user, product=product.product_id).exists()
            at = random_datetime()

            # 중복 체크를 위한 현재 조합의 키 생성
            current_combination = (user.user_id, product.product_id)

            if not love_exists and current_combination not in existing_combinations:
                product.count_love += 1
                to_update_count_love.append(product)
                user_log = models.UserLog(
                    created_who=user.user_id,
                    name=user.name,
                    created_at=at,
                    doit="LOVE",
                    product_id=product.product_id
                )
                love = models.Love(
                    created_at=at,
                    created_who=user,
                    product_id=product.product_id
                )
                to_create_user_log.append(user_log)
                to_create_love.append(love)
                existing_combinations.add(current_combination)

        models.UserLog.objects.bulk_create(to_create_user_log)
        models.Love.objects.bulk_create(to_create_love)
        models.Product.objects.bulk_update(to_update_count_love, fields=['count_love'])
