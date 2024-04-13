from django.core.management.base import BaseCommand
from django.db import transaction
from Existing_db import models
import random


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        products = models.Product.objects.all()
        sizes = ['S','M','L','XL','XXL']
        to_create = []
        for product in products:
            for size in sizes:
                detail = models.ProductDetail(product_id=product.product_id
                                              ,size=size, pd_before_count=random.randint(3,100)
                                              ,pd_sell_count=(random.randint(10,1000)))
                to_create.append(detail)
        models.ProductDetail.objects.bulk_create(to_create)