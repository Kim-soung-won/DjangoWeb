import random
from django.utils import timezone
from datetime import timedelta, datetime


def random_datetime():
    start_date = timezone.make_aware(datetime(2024, 1, 1, 0, 0, 0))
    end_date = timezone.make_aware(datetime(2024, 4, 1, 23, 59, 59))
    delta = end_date - start_date
    random_second = random.randint(0, int(delta.total_seconds()))
    random_date = start_date + timedelta(seconds=random_second)
    return random_date
