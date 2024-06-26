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
        for j in range(100):

            for i in range(100):
                print(i)
                rand: int = random.randint(1, 5000)
                user = models.UserInfo.objects.get(user_id=rand)
                rand: int = random.randint(0, 100)
                product = products[rand]
                love_exists = models.Love.objects.filter(created_who=user, product=product.product_id).exists()
                at = random_datetime()

                if not love_exists:
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

            models.UserLog.objects.bulk_create(to_create_user_log)
            models.Love.objects.bulk_create(to_create_love)
            models.Product.objects.bulk_update(to_update_count_love, fields=['count_love'])
