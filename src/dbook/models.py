from django.db import models
from dbase.models import Author, Book_series, Genre, Publisher

# Create your models here.
class Book(models.Model):
    bookname = models.CharField(
        verbose_name='Название книги',
        max_length=200,
        blank=False,
        null=False
        )
    foto = models.ImageField(
        verbose_name='Фото книги',
        blank=True,
        null=True   
    )
    price = models.FloatField(
        verbose_name='Цена книги',
        blank=True,
        null=True   
    )
    author = models.ManyToManyField(
        Author,
        verbose_name='Авторы',
        blank=True
    )
    serie = models.ForeignKey(
        Book_series,
        verbose_name='Книжная серия',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр книги',
        blank=True
    )
    publication_year = models.CharField(
        verbose_name='Год издания',
        max_length=4,
        blank=True,
        null=True   
    )
    pages = models.IntegerField(
        verbose_name='Количество страниц',
        blank=True,
        null=True
    )
    bind = models.CharField(
        verbose_name='Переплет',
        max_length=100,
        blank=True,
        null=True           
    )
    form = models.CharField(
        verbose_name='Формат',
        max_length=100,
        blank=True,
        null=True   
    )
    isbn = models.CharField(
        verbose_name='ISBN',
        max_length=13,
        blank=True,
        null=True   
    )
    weigt = models.IntegerField(
        verbose_name='Вес книги',
        blank=True,
        null=True   
    )
    age_limit = models.CharField(
        verbose_name='Возрастные ограничения',
        max_length=3,
        blank=True,
        null=True   
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.PROTECT,
        verbose_name='Издательство',
        max_length=200,
        blank=True,
        null=True
        )
    books_available = models.IntegerField(
        verbose_name='Количество книг в наличии',
        blank=False,
        null=False
    )
    active_choises = (
        (True, 'Доступна'),
        (False, 'Недостпна')
    )
    active = models.BooleanField(
        verbose_name='Доступна для заказа',
        choices=active_choises,
        blank=False,
        null=False
    )
    rating = models.FloatField(
        verbose_name='Рейтинг книги',
        blank=True,
        null=True
    )
    add_date = models.DateField(
        auto_now_add=True,
        verbose_name = 'Дата создания'
    )
    change_date = models.DateField(
        auto_now=True,
        verbose_name = 'Дата последнего изменения'
    )

    def __str__(self):
       return (self.bookname)