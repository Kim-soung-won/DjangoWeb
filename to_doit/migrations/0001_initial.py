# Generated by Django 4.2.11 on 2024-03-18 02:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('name', models.CharField(default='', max_length=20, verbose_name='작업 이름')),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='시작날짜')),
                ('end_date', models.DateField(null=True, verbose_name='마감날짜')),
                ('finish_date', models.DateField(null=True, verbose_name='완료날짜')),
                ('state', models.IntegerField(default=0, verbose_name='상태')),
            ],
            options={
                'verbose_name': 'to-do 테이블',
                'db_table': 'task',
            },
        ),
    ]
