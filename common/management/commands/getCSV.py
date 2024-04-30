import csv
from Existing_db import models
from django.core.management.base import BaseCommand
import logging

logger = logging.getLogger('django')


class Command(BaseCommand):
    help = 'Export Product data to CSV file'

    def handle(self, *args, **options):
        try:
            logger.info("Start GET CSV")
            output_csv_file_path = 'common/products.csv'
            products = models.Product.objects.all()

            with open(output_csv_file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                writer.writerow(['product_id', 'product_name', 'product_price', 'brand_id', 'product_category'
                                    , 'created_who', 'created_at', 'count_love'])

                for instance in products:
                    writer.writerow([
                        getattr(instance, 'product_id'),
                        getattr(instance, 'product_name'),
                        getattr(instance, 'product_price'),
                        getattr(instance, 'brand_id'),
                        getattr(instance, 'product_category'),
                        getattr(instance, 'created_who'),
                        getattr(instance, 'created_at'),
                        getattr(instance, 'count_love')
                    ])
            self.stdout.write(self.style.SUCCESS('Successfully'))
            logger.info("GET CSV Successfully")
        except Exception as e:
            error_message = f"Failed to export product data to CSV. Error: {str(e)}"
            self.stdout.write(self.style.ERROR(error_message))
            logger.error(error_message)
