from django.db import models

# Create your models here.

# class Adress(models.Model):
#     country = models.CharField(
#         verbose_name='Страна',
#         max_length=30,
#         blank=False,
#         null=False
#     )
#     city = models.CharField(
#         verbose_name='Страна',
#         max_length=30,
#         blank=False,
#         null=False
#     )
#     postindex = models.CharField(
#         verbose_name='Страна',
#         max_length=30,
#         blank=False,
#         null=False
#     )
#     adress1 = models.CharField(
#         verbose_name='Страна',
#         max_length=30,
#         blank=False,
#         null=False
#     )    
#     adress2 = models.CharField(
#         verbose_name='Страна',
#         max_length=30,
#         blank=False,
#         null=False
#     )  

# class Persone_type(models.Model):
#     admin = 'AD'
#     manager = 'MN'
#     customer = 'CU'
#     person_choice = [
#         (admin, 'Администратор'),
#         (manager, 'Менеджер'),
#         (customer, 'Покупатель'),
#         ]
#     persone_type = models.CharField(
#         verbose_name='Группа пользователей',
#         max_length=30,
#         choices = person_choice,
#         default = customer,
#         )    


    

# class Customer(models.Model):
#     login = models.CharField(
#         verbose_name='Имя',
#         max_length=30
#     )
#     password = models.CharField(
#         verbose_name='Имя',
#         max_length=30
#     )
#     email = models.EmailField(
#         verbose_name='Электронная почта',
#         max_length=30
#     )
#     first_name = models.CharField(
#         verbose_name='Имя',
#         max_length=30
#     )
#     last_name = models.CharField(
#         verbose_name='Фамилия',
#         max_length=30
#     )
#     adress = models.ForeignKey(
#         Adress,
#         on_delete=models.PROTECT
#     )

#     def __str__(self):
#         return (self.last_name)

class Author(models.Model):
    author_name = models.CharField(
        verbose_name='Автор',
        max_length=50
    )
    author_pseudonym = models.CharField(
        verbose_name='Псевдонимы',
        max_length=50
    )
    author_comments = models.CharField(
        verbose_name='Комментарии',
        max_length=500
    )

class Book_series(models.Model):
    series = models.CharField(
        verbose_name='Книжная серия',
        max_length=100,
        blank=True,
        null=True
        )    

class Genre(models.Model):
    genre = models.CharField(
        verbose_name='Жанры',
        max_length=50,
        blank=True,
        null=True
        ) 
    description = models.CharField(
        verbose_name='Описание жанра',
        max_length=500,
        blank=True,
        null=True
        )

class Publisher(models.Model):
    publisher = models.CharField(
        verbose_name='Издательство',
        max_length=100,
        blank=False,
        null=False
        )
    publisher_desc = models.CharField(
        verbose_name='Информация об издательстве',
        max_length=500,
        blank=True,
        null=True
        )

# class Book(models.Model):
#     bookname = models.CharField(
#         verbose_name='Название книги',
#         max_length=200,
#         blank=False,
#         null=False
#         )
    # foto
    # price
    # publication_year
    # pages
    # bind
    # form
    # isbn
    # weigt
    # age_limit
    # publisher = models.ForeignKey(
    #     Publisher,
    #     on_delete=models.PROTECT,
    #     verbose_name='Книжная серия',
    #     max_length=200,
    #     blank=False,
    #     null=False
    #     )
    # books_available
    # active
    # rating 
    # add_date
    # change_date



    

