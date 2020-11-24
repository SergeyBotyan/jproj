from django.db import models
from django.contrib.auth import get_user_model

from dbook.models import Book
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
       return (self.customer)

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

    # class Order(models.Model):
    #     book = models.ForeignKey(
    #         Book,
    #         related_name='order',
    #         on_delete=models.PROTECT,
    #         blank=True,
    #         null=True
    #     )   
    #     quantity = models.IntegerField(
    #         'Quantity',
    #         default=1
    #     )     
