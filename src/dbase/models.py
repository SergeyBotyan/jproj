from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(
        verbose_name='Автор',
        max_length=50,
        blank=False,
        null=False
    )
    pseudonym = models.CharField(
        verbose_name='Псевдонимы',
        max_length=50,
        blank=True,
        null=True
    )
    comments = models.CharField(
        verbose_name='Комментарии',
        max_length=500,
        blank=True,
        null=True
    )
    
    def __str__(self):
       return (self.name)

class Book_series(models.Model):
    name = models.CharField(
        verbose_name='Книжная серия',
        max_length=100,
        blank=False,
        null=False
        )

    def __str__(self):
       return (self.name)    

class Genre(models.Model):
    name = models.CharField(
        verbose_name='Жанры',
        max_length=50,
        blank=False,
        null=False
        ) 
    description = models.CharField(
        verbose_name='Описание жанра',
        max_length=500,
        blank=True,
        null=True
        )

    def __str__(self):
       return (self.name)

class Publisher(models.Model):
    name = models.CharField(
        verbose_name='Издательство',
        max_length=100,
        blank=False,
        null=False
        )
    description = models.CharField(
        verbose_name='Информация об издательстве',
        max_length=500,
        blank=True,
        null=True
        )

    def __str__(self):
       return (self.name)





    

