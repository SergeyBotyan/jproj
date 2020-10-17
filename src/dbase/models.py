from django.db import models

# Create your models here.

class Adress(models.Model):
    country = models.CharField(
        verbose_name='Страна',
        max_length=30,
        blank=False,
        null=False
        )
    city = models.CharField(
        verbose_name='Страна',
        max_length=30,
        blank=False,
        null=False
        )
    postindex = models.CharField(
        verbose_name='Страна',
        max_length=30,
        blank=False,
        null=False
        )
    adress1 = models.CharField(
        verbose_name='Страна',
        max_length=30,
        blank=False,
        null=False
        )    
    adress2 = models.CharField(
        verbose_name='Страна',
        max_length=30,
        blank=False,
        null=False
        )        

class Persone(models.Model):
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=30
        )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=30
        )
    adress = models.ForeignKey(
        Adress,
        on_delete=models.CASCADE
        )

    def __str__(self):
        return self.last_name
