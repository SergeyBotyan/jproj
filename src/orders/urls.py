from django.conf.urls.static import static
from django.conf import settings
from django.urls import path


from orders.views import *

app_name = 'orders'

urlpatterns = [
    path('delete-book-in-cart/<int:pk>', DeleteBookInCart.as_view(), name='delete-book-in-cart'),
    path('update-cart', UpdateCart.as_view(), name='update-cart'),
    path('order-view', OrderView.as_view(), name='order-view'),
    path('order-checkout', OrderCheckout.as_view(), name='order-checkout'),
    path('delete-order/<int:pk>', DeleteOrder.as_view(), name='delete-order'),
    path('edit-order/<int:pk>', OrderEditView.as_view(), name='edit-order'),
    path('', CartView.as_view(), name='cart'),
]