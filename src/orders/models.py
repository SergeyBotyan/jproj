from django.db import models
from django.contrib.auth import get_user_model

from dbook.models import Book
from user.models import Profile, Adress
# Create your models here.

User = get_user_model()

class Cart(models.Model):
    customer = models.ForeignKey(
       User,
       related_name='carts',
       on_delete=models.PROTECT,
       blank=True,
       null=True
    )
    created_date = models.DateTimeField(
        verbose_name='Дата создания корзины',
        auto_now=False,
        auto_now_add=True
    )
    last_edit_date = models.DateTimeField(
        verbose_name='Дата последнего редактирования',
        auto_now=True,
        auto_now_add=False
    )

    def total_price(self):
        price = 0
        for books in self.books.all():
            price += books.price
        return price


    def __str__(self):
       return f'{self.pk} - {self.customer} - {self.last_edit_date}'

class BookInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='books'
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.PROTECT,
        related_name='books_in_carts'
    )
    quantity = models.IntegerField(
        'Quantity',
        default=1
    )
    price = models.DecimalField(
        'Price',
        decimal_places=2,
        max_digits=5
    )
    created_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now=False,
        auto_now_add=True
    )
    last_edit_date = models.DateTimeField(
        verbose_name='Дата последнего редактирования',
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self):
       return f'{self.book.name}'

    def construct_price(self):
        price = self.quantity * self.book.price
        return price

class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='orders'
    )
    profile = models.ForeignKey(
        Profile,
        on_delete=models.PROTECT,
        related_name='orders'
    )
    adress = models.ForeignKey(
        Adress,
        on_delete=models.PROTECT,
        related_name='orders'
    )
    total_price = models.DecimalField(
        'Order price',
        decimal_places=2,
        max_digits=5        
    )
    status_choices = (
    ('1 - Сформирован', '1 - Сформирован'),
    ('2 - Подтвержден', '2 - Подтвержден'),
    ('3 - Выполняется', '3 - Выполняется'),
    ('4 - Выполнен', '4 - Выполнен')
    )
    status = models.CharField(
        verbose_name='Статус заказа',
        max_length=15,
        choices=status_choices,
        default='1 - Сформирован',
        blank=False,
        null=False
    )
    information = models.CharField(
        verbose_name='Дополнительная информация',
        max_length=200,
        blank=True,
        null=True
    )
    created_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now=False,
        auto_now_add=True
    )
    last_edit_date = models.DateTimeField(
        verbose_name='Дата последнего редактирования',
        auto_now=True,
        auto_now_add=False
    )    

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ №{self.id}'

    def get_total_price(self):
        cost = 0
        for bio in self.bio.all():
            cost += bio.price
        return cost


class BookInOrder(models.Model):
    order = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE, 
        related_name='bio'
        )
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE, 
        related_name='bio'
        )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.quantity
