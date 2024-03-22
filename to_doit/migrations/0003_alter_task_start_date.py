# Generated by Django 4.2.11 on 2024-03-21 02:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('to_doit', '0002_alter_task_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='시작날짜'),
        ),
    ]
