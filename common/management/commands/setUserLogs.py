import random
from django.core.management.base import BaseCommand
from django.db import transaction
from Existing_db import models
from django.utils import timezone
from datetime import timedelta, datetime


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        for i in range(100000):
            random_user = models.UserInfo.objects.order_by('?').first()
            random_product = models.Product.objects.order_by('?').first()
            actions = ["SAW", "LOVE", "PAYMENT"]
            random_action = random.choice(actions)
            log = models.UserLog.objects.create(
                created_who=random_user.user_id,
                name=random_user.name,
                created_at=random_datetime(),
                doit=random_action,
                product_id=random_product.product_id
            )
            print(i)


def random_datetime():
    start_date = timezone.make_aware(datetime(2024, 3, 1))
    end_date = timezone.make_aware(datetime(2024, 4, 5))
    delta = end_date - start_date
    random_second = random.randint(0, int(delta.total_seconds()))
    random_date = start_date + timedelta(seconds=random_second)
    return random_date
