from django.core.management.base import BaseCommand
from django.db import transaction
from Existing_db import models

class SetUserInfo(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        users = models.UserAccount.objects.all()
        userInfos = models.UserInfo.objects.all()
        id_list = []
        for infos in userInfos:
            id_list.append(infos.user_id)
        for user in users:
            if user.user_id in id_list:
                continue
            user_info = models.UserInfo.objects.create(user_id=user.user_id,name=user.user_email)
            print(user_info.user_id)