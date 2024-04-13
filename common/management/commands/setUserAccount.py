from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from datetime import timedelta, datetime
import random
from Existing_db import models


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        users = models.UserAccount.objects.all()
        compare_date = timezone.make_aware(datetime(2024,3,30))
        for i in range(1,5000):
            user = models.UserAccount.objects.create(
                user_email="test"+str(i),
                user_password="testPwd"+str(i),
                user_role="USER",
                user_pnum="1234-1234",
                last_login=random_datetime()
            )


def random_datetime():
    start_date = timezone.make_aware(datetime(2024, 3, 1))
    end_date = timezone.make_aware(datetime(2024, 4, 5))
    delta = end_date - start_date
    random_second = random.randint(0, int(delta.total_seconds()))
    random_date = start_date + timedelta(seconds=random_second)
    return random_date



