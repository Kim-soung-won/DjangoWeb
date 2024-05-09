import random
from django.db import transaction
from Existing_db import models
from django.core.management.base import BaseCommand

from common.SettingDummyData.RandomDateTime import random_datetime


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        products = models.Product.objects.all()
        to_create_comment = []
        comments = ["야호~!~! 댓글 창이닸!!", "히히 좋댓구알~", "이 댓글들은 랜덤으로 생긴거에여"
            , "반가워요", "그립습니다. 지훈, 건우...", "모코코는 초록색", "배고프다",
                    "꺄르르르르", "옷 관련 댓글은 없는건가요?", "이 사이트 참 좋군요"
            , "모꼬로로로롞", "made by 승훈,수연,원근,승원"]
        for i in range(1000):
            print(i)
            rand: int = random.randint(1, 5000)
            user = models.UserInfo.objects.get(user_id=rand)
            rand: int = random.randint(0, 100)
            product = products[rand]
            at = random_datetime()

            comment = models.Comment(
                product_id=product.product_id,
                created_who=user,
                created_at=at,
                content=random.choice(comments),
                created_name=user.name
            )
            to_create_comment.append(comment)

        models.Comment.objects.bulk_create(to_create_comment)
