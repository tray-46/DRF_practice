from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Breed(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название породы", help_text="Укажите название породы")
    description = models.TextField(
        null=True, blank=True, verbose_name="Описание породы", help_text="Укажите описание породы"
    )
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Владелец",
                              help_text="Укажите владельца")

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"

    def __str__(self) -> str:
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=100, verbose_name="Кличка", help_text="Укажите кличку")
    breed = models.ForeignKey(
        Breed, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Порода", help_text="Выберите породу"
    )
    photo = models.ImageField(
        upload_to="dogs/photo/", null=True, blank=True, verbose_name="Фото", help_text="Загрузите фото собаки"
    )
    date_born = models.DateField(
        null=True, blank=True, verbose_name="Дата рожддения", help_text="Укажите дату рождения"
    )
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Владелец",
                              help_text="Укажите владельца собаки")
    likes = models.ManyToManyField(User, related_name="users_likes", null=True, blank=True)

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"

    def __str__(self) -> str:
        return self.name


class Donation(models.Model):
    amount = models.PositiveIntegerField(verbose_name="Сумма пожертвования", help_text="Укажите сумму пожертвования")
    session_id = models.CharField(max_length=255, null=True, blank=True, verbose_name="Id сессии",
                                  help_text="Укажите id сесси")
    link = models.URLField(max_length=500, null=True, blank=True, verbose_name="Ссылка на оплату")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Пользователь")

    class Meta:
        verbose_name = "Пожертвование"
        verbose_name_plural = "Пожертвования"

    def __str__(self) -> str:
        return self.amount
