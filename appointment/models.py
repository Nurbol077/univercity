from django.db import models


class Appointment(models.Model):
    guardian_name = models.CharField(
        max_length=255,
        verbose_name='Имя родителей'
    )
    guardian_email = models.EmailField(
        verbose_name='Email родителя'
    )
    child_name = models.CharField(
        max_length=255,
        verbose_name='Имя ребенка'
    )
    child_age = models.PositiveSmallIntegerField(
        verbose_name='Возраст ребенка'
    )
    message = models.TextField()

    def __str__(self):
        return f'{self.guardian_name} - {self.child_age}'

    class Meta:
        verbose_name = 'Запись на прием'
        verbose_name_plural = 'Записи на приемы'


class Review(models.Model):
    client_image = models.ImageField(
        verbose_name='Фотография клиента',
        upload_to='client_image/'
    )
    client_name = models.CharField(
        verbose_name='ФИО клиента',
        max_length=255
    )
    role = models.CharField(
        verbose_name='Профессия клиента',
        max_length=255
    )
    text = models.TextField(
        verbose_name='Отзыв'
    )