from django.utils import timezone
import random
from django.core.management.base import BaseCommand
from django.db import transaction
from Existing_db import models


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        user_ids = list(models.UserAccount.objects.values_list('user_id', flat=True))
        selected_ids = random.sample(user_ids, 1000)

        print(selected_ids)

        selected_users = models.UserAccount.objects.filter(user_id__in=selected_ids)

        current_time = timezone.now()
        for user in selected_users:
            user.last_login = current_time
        models.UserAccount.objects.bulk_update(selected_users, ['last_login'])