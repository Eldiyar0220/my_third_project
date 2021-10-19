from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(email, password, **extra_fields)



class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=250)
    before_last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=13)

    city = models.CharField(max_length=150)
    address_living = models.CharField(max_length=250)
    number_of_address = models.CharField(max_length=13)
    postal_code = models.CharField(max_length=150, null=False, blank=False)
    telegram = models.CharField(max_length=150)
    activation_code = models.CharField(max_length=8, blank=True)


    # passport_out = models.ImageField(upload_to='scan_out')
    # passport_in = models.ImageField(upload_to='scan_in')
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    good = models.BooleanField(default=False)


    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.email}'

    def create_activation_code(self):
        from django.utils.crypto import get_random_string
        code = get_random_string(8, '0123456789')
        self.activation_code = code
        self.save()

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, perm, obj=None):
        return self.is_staff



# TODO do not forget about Скан паспорт