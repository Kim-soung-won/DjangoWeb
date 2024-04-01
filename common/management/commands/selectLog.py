from django.core.management.base import BaseCommand
from django.db import transaction
from Existing_db import models


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        users = models.UserInfo.objects.all()
        for user in users:
            categories = []
            logs = models.UserLog.objects.filter(created_who=user.user_id)
            print(logs.count())
            for log in logs:
                if log.product_id == None:
                    continue
                product = models.Product.objects.get(product_id=log.product_id)
                categories.append(product.pd_category)
            category_str = ",".join(categories)
            print(user.user_id)
            models.Recommend.objects.create(created_who=user, product_list=category_str)

            
