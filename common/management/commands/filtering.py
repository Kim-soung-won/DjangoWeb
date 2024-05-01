import pandas as pd
import pickle
from django.core.management.base import BaseCommand
import logging

logger = logging.getLogger('django')


class Command(BaseCommand):
    help = 'Filter'

    def handle(self, *args, **options):
        try:
            logger.info("Start Filtering GET pickle Successfully")
            df1 = pd.read_csv('common/products.csv', encoding='utf-8')

            indices = pd.Series(df1.index, index=df1['product_id']).drop_duplicates()
            print(indices)

            products = df1[['product_id', 'product_category']].copy()
            pickle.dump(products, open('common/product.pickle', 'wb'))
            self.stdout.write(self.style.SUCCESS('Filterring Successfully'))
            logger.info("Filtering Successfully")
        except Exception as e:
            error_message = f"Failed to Filtering to pickle. Error: {str(e)}"
            self.stdout.write(self.style.ERROR(error_message))
            logger.error(error_message)
