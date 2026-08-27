from django.db import models


# Create your models here.
class Breed(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название породы", help_text="Укажите название породы")
    description = models.TextField(
        null=True, blank=True, verbose_name="Описание породы", help_text="Укажите описание породы"
    )

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

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"

    def __str__(self) -> str:
        return self.name
