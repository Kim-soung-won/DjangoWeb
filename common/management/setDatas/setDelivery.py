import random
from django.db import transaction
from Existing_db import models
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta, datetime

from common.SettingDummyData.RandomDateTime import random_datetime


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        start_date = timezone.make_aware(datetime(2024, 1, 1, 0, 0, 0))
        end_date = timezone.make_aware(datetime(2024, 4, 1, 23, 59, 59))
        payments = models.Payment.objects.filter(created_at__range=(start_date, end_date))
        list = []
        for payment in payments:
            id = payment.payment_id
            at = random_datetime()
            delivery = models.Delivery(
                payment_id=id,
                tg_address='임시 주소',
                tg_pnum='임시 연락처',
                state='COMPLETE',
                created_at=at,
                updated_at=at+timedelta(days=4)
            )
            list.append(delivery)
        models.Delivery.objects.bulk_create(list)



