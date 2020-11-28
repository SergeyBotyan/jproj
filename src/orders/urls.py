from django.conf.urls.static import static
from django.conf import settings
from django.urls import path


from orders.views import CartView, DeleteBookInCart, UpdateCart, OrderView

app_name = 'orders'

urlpatterns = [
    path('delete-book-in-cart/<int:pk>', DeleteBookInCart.as_view(), name='delete-book-in-cart'),
    path('update-cart', UpdateCart.as_view(), name='update-cart'),
    path('order-view', OrderView.as_view(), name='order-view'),
    path('', CartView.as_view(), name='cart'),
]