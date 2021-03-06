# Generated by Django 3.2.7 on 2021-12-14 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(blank=True, max_length=150)),
                ('last_name', models.CharField(max_length=250)),
                ('before_last_name', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=13)),
                ('city', models.CharField(max_length=150)),
                ('address_living', models.CharField(max_length=250)),
                ('number_of_address', models.CharField(max_length=13)),
                ('postal_code', models.CharField(max_length=150)),
                ('telegram', models.CharField(max_length=150)),
                ('activation_code', models.CharField(blank=True, max_length=8)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('good', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
