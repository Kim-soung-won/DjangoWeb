# Generated by Django 4.2.11 on 2024-03-16 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_loginuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='email',
            field=models.CharField(max_length=255, null=True, verbose_name='이메일 주소'),
        ),
        migrations.AlterField(
            model_name='loginuser',
            name='name',
            field=models.CharField(max_length=20, null=True, verbose_name='이름'),
        ),
    ]
