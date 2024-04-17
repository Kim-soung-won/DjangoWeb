from datetime import datetime, timedelta
from django.utils import timezone
from django.core.management.base import BaseCommand
from django.db import transaction
from Existing_db import models
import random

from common.SettingDummyData.RandomDateTime import random_datetime


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        products = models.Product.objects.all()
        sizes = ['S', 'M', 'L', 'XL', 'XXL']
        to_create = []
        categorys = []
        categorys.append(["캐주얼", "포멀", "비즈니스", "빈티", "럭셔리", "스트리트", "러프", "귀여운", "세련된", "고전적인", "펑키", "힙스터", "스포츠", "레트로", "보헤미안",
               "고급스러운", "모던", "미니멀리스트", "유니크", "클래식", "편안한", "트디", "아방가르드"])
        categorys.append(["코튼", "실크", "데님", "리넨", "울", "가죽", "플리스", "캐시미어", "벨벳", "코듀로이", "트위드", "폴리에스테르", "레이온", "잔스", "니트", "카모플라지", "지퍼", "체크", "스트라이프", "패턴"])
        categorys.append(["블랙", "화이트", "레드", "블루", "그린", "옐로우", "핑크", "오렌지", "퍼플", "브라운", "그레이", "골드", "실버", "네이비", "버건디", "테일", "머스타드", "카키", "민트", "로즈골드"])
        categorys.append(["S", "M", "L", "XL", "XXL", "Plus Size", "Petite Size", "Custom Size", "Loose Fit", "Slim Fit", "Regular Fit"])
        categorys.append(["봄", "여름", "가을", "겨울", "시즌오프", "신상품", "할인상품"])
        categorys.append(["비즈니스", "파티", "데이트", "캐주얼", "비치", "클럽", "스포츠", "학교", "집", "여행", "피트니스", "헬스", "요가"])
        categorys.append(["상의", "하의", "아우터", "원피스", "언더웨어", "액세서리"])
        categorys.append(["국내브랜드", "해외브랜드", "디자이너브랜드", "고급브랜드", "저렴한 브랜드", "유명브랜드", "럭셔리브랜드"])
        categorys.append(["이코프렌드리", "핸드메이드", "리사이클", "오가닉", "비건", "지속가능한", "한정판", "커스텀메이드"])
        categorys.append(["여성", "남성", "어린이", "청소년", "어른", "실버세대", "신혼부부", "대학생", "직장인", "유아", "임산부"])
        for i in range(50,5001):
            print(i)
            category = ""
            for j in range(10):
                category += random.choice(categorys[j])+","
            product = models.Product(product_id=i,
                                     pd_name=str(i)+"번옷",
                                     brand_id=random.randint(1,10),
                                     created_at=random_datetime(),
                                     price=random.randint(10000,500000),
                                     created_who=11,
                                     pd_category=category)
            to_create.append(product)
        models.Product.objects.bulk_create(to_create)

