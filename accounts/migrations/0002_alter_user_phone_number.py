# Generated by Django 3.2.7 on 2021-10-11 13:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message='Формат номера: 996 999 999 999', regex='^(996)\\d{9}$')]),
        ),
    ]