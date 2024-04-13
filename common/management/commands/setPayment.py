import random
from django.db import transaction
from Existing_db import models
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta, datetime


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        products = models.ProductDetail.objects.all()
        to_create = []
        to_create_log = []
        to_create_user_log = []
        to_update = []
        for i in range(len(products)):
            print(i)
            rand: int = random.randint(1, 5000)
            print(rand)
            user = models.UserInfo.objects.get(user_id=rand)
            rand: int = random.randint(0, len(products) - 1)
            product_detail = products[rand]
            product = models.Product.objects.get(product_id=product_detail.product_id)
            count = random.randint(1, 5)
            at = random_datetime()
            product_detail.pd_sell_count += count
            to_update.append(product_detail)
            payment = models.Payment(
                created_who=user,
                product_id=product.product_id,
                count=count,
                total_price=product.pd_price * count,
                size=product_detail.size,
                created_at=at
            )
            product_log = models.ProductLog(
                product_id=product.product_id,
                created_who=user,
                count=count * (-1),
                created_at=at,
                size=product_detail.size
            )
            user_log = models.UserLog(
                created_who=user.user_id,
                name=user.name,
                created_at=at,
                doit="PAYMENT",
                product_id=product.product_id
            )
            to_create.append(payment)
            to_create_log.append(product_log)
            to_create_user_log.append(user_log)
        models.Payment.objects.bulk_create(to_create)
        models.UserLog.objects.bulk_create(to_create_user_log)
        models.ProductLog.objects.bulk_create(to_create_log)
        models.ProductDetail.objects.bulk_update(to_update, ['pd_sell_count'])


def random_datetime():
    start_date = timezone.make_aware(datetime(2024, 1, 1, 0, 0, 0))
    end_date = timezone.make_aware(datetime(2024, 4, 1, 23, 59, 59))
    delta = end_date - start_date
    random_second = random.randint(0, int(delta.total_seconds()))
    random_date = start_date + timedelta(seconds=random_second)
    return random_date
