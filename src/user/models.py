from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE
        )
    adress = models.CharField(
        verbose_name='Адрес',
        max_length=200,
        blank=True,
        null=True
        )
    phone1 = models.CharField(
        verbose_name='Телефон1',
        max_length=13,
        blank=True,
        null=True
        )
    phone2 = models.CharField(
        verbose_name='Телефон2',
        max_length=13,
        blank=True,
        null=True
        )

    