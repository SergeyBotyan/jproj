from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name='profile'
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
    information = models.CharField(
        verbose_name='Дополнительная информация',
        max_length=200,
        blank=True,
        null=True
        )

class Adress(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='adress'
        )
    country = models.CharField(
        verbose_name='Страна',
        max_length=13
        )
    sity = models.CharField(
        verbose_name='Город',
        max_length=20
        )
    post_index = models.IntegerField(
        verbose_name='Почтовый индекс',
        blank=True,
        null=True
        )
    adress = models.CharField(
        verbose_name='Адрес доставки',
        max_length=50
        )

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    

    