from django.db import models
from django.utils import timezone


class Task(models.Model):
    user_id = models.CharField(max_length=20, null=False, blank=False)
    name = models.CharField(max_length=20, verbose_name="작업 이름", null=False, default='')
    start_date = models.DateField(verbose_name="시작날짜", default=timezone.now)
    end_date = models.DateField(verbose_name="마감날짜", null=True)
    finish_date = models.DateField(verbose_name="완료날짜", null=True)
    state = models.IntegerField(verbose_name="상태", null=False, default=0)

    class Meta:
        db_table = "task"
        verbose_name = "to-do 테이블"