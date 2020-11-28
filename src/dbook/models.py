from django.db import models

from dbase.models import Author, Book_series, Genre, Publisher


def image_upload_path(instance, filename):
    print('book_images/{0}_{1}'.format(instance.id, filename))
    return 'book_images/{0}_{1}'.format(instance.id, filename)

# Create your models here.
class Book(models.Model):
    name = models.CharField(
        verbose_name='Название книги',
        max_length=200,
        blank=False,
        null=False
        )
    foto = models.ImageField(
        verbose_name='Фото книги',
        upload_to=image_upload_path,
        default='book_images/no_image.jpg',
        blank=True,
        null=True   
    )
    price = models.DecimalField(
        verbose_name='Цена книги',
        decimal_places=2,
        max_digits=5   
    )
    author = models.ManyToManyField(
        Author,
        verbose_name='Авторы',
        related_name='books',
        blank=False
    )
    series = models.ForeignKey(
        Book_series,
        verbose_name='Книжная серия',
        on_delete=models.PROTECT,
        related_name='books',
        blank=True,
        null=True
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр книги',
        related_name='books',
        blank=False
    )
    publication_year = models.CharField(
        verbose_name='Год издания',
        max_length=4,
        blank=False,
        null=False  
    )
    pages = models.IntegerField(
        verbose_name='Количество страниц',
        blank=False,
        null=False
    )
    bind = models.CharField(
        verbose_name='Переплет',
        max_length=100,
        blank=False,
        null=False          
    )
    form = models.CharField(
        verbose_name='Формат',
        max_length=100,
        blank=False,
        null=False  
    )
    isbn = models.CharField(
        verbose_name='ISBN',
        max_length=13,
        blank=True,
        null=True   
    )
    weight = models.IntegerField(
        verbose_name='Вес книги',
        blank=False,
        null=False   
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
        related_name='books',
        blank=False,
        null=False
        )
    books_available = models.IntegerField(
        verbose_name='Количество книг в наличии',
        blank=False,
        null=False
    )
    active_choises = (
        (True, 'Доступна'),
        (False, 'Недоступна')
    )
    active = models.BooleanField(
        verbose_name='Доступна для заказа',
        choices=active_choises,
        blank=False,
        null=False
    )
    rating = models.FloatField(
        verbose_name='Рейтинг книги',
        blank=False,
        null=False,
        default=0
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
       return f'{self.pk} {self.name}'

    def __unicode__(self):
      return self.foto.url
