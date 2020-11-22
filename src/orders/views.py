from django.views.generic import ListView, DeleteView, RedirectView
from django.contrib.auth.models import User
from django.urls import reverse_lazy


from .models import Cart, BookInCart
from dbook.models import Book


# Create your views here.

def create_cart(user, session):
    cart = Cart.objects.create(customer=user)
    session['cart_id'] = cart.pk
    return cart

class CartView(ListView):
    model=Cart
    template_name='orders/cart.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        """Get the context for this view."""
        queryset = object_list if object_list is not None else self.object_list
        page_size = self.get_paginate_by(queryset)
        context_object_name = self.get_context_object_name(queryset)
        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
            context = {
                'paginator': paginator,
                'page_obj': page,
                'is_paginated': is_paginated,
                'object_list': queryset
            }
        else:
            context = {
                'paginator': None,
                'page_obj': None,
                'is_paginated': False,
                'object_list': queryset
            }
        if context_object_name is not None:
            context[context_object_name] = queryset
        context.update(kwargs)
        cart_id = self.request.session.get('cart_id')
        user = self.request.user
        if not isinstance(user, User):
            user = None
        if cart_id:
            cart = Cart.objects.filter(pk=cart_id).first()
            if not cart:
                cart = create_cart(user, self.request.session)
        else:
            cart = create_cart(user, self.request.session)
        context['cart'] = cart
        book_id = self.request.GET.get('book')
        if not book_id:
            return context
        book = Book.objects.filter(pk=int(book_id)).first()
        if book:
            book_in_cart, created = BookInCart.objects.get_or_create(
                book=book,
                cart=cart,
                defaults={
                    'quantity':1,
                    'price':book.price
                }
            )
            if not created:
                book_in_cart.quantity = book_in_cart.quantity + 1
                book_in_cart.price = book_in_cart.construct_price()
                book_in_cart.save()
        #add to the cart
        else:
            pass #redirect INFA NO BOOK

        context['book'] = book
        return super().get_context_data(**context)

class DeleteBookInCart(DeleteView):
    model=BookInCart
    template_name='orders/delete-book-in-cart.html'
    success_url = '/orders'

class UpdateCart(RedirectView):
    def get_redirect_url(self):
        #get the cart
        cart_id = self.request.session.get('cart_id')
        user = self.request.user
        if cart_id:
            cart = Cart.objects.filter(pk=cart_id).first()
        else:
            #redirect to error page
            pass
            self.request.POST.get('checkout')

        return reverse_lazy('orders:cart')
