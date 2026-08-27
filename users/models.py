from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):

    email = models.EmailField(unique=True, verbose_name="Почта", help_text="Укажите почту")
    phone = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="Номер телефона", help_text="Укажите номер телефона"
    )
    telegram = models.CharField(
        max_length=32, null=True, blank=True, verbose_name="Телеграм ник", help_text="Укажите ник в Телеграм"
    )
    avatar = models.ImageField(
        upload_to="users/avatars/", null=True, blank=True, verbose_name="Аватар", help_text="Загрузите аватар"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
