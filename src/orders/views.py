from django.views.generic import ListView, DeleteView, RedirectView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Cart, BookInCart, Order, BookInOrder
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
            pass #redirect INF NO BOOK

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
        button = self.request.POST.get('submit_button')
        if button == 'edit':
            obj_list = []
            for book_in_cart_id, quantity in self.request.POST.items():
                if book_in_cart_id not in ['csrfmiddlewaretoken', 'submit_button']:
                    book_in_cart = BookInCart.objects.get(pk = int(book_in_cart_id))
                    if book_in_cart.cart.pk == cart.id:
                        book_in_cart.quantity = int(quantity)
                        obj_list.append(book_in_cart)
                        book_in_cart.price = book_in_cart.construct_price()
            BookInCart.objects.bulk_update(obj_list, ['quantity'])
            BookInCart.objects.bulk_update(obj_list, ['price'])
            return reverse_lazy('orders:cart')
        elif button == 'checkout':
            if user.is_anonymous:
                # redirect to create user
                return reverse_lazy('accounts:register')
            
            if user.adress:
                new_order = Order.objects.create(
                    user=user,
                    profile=user.profile,
                    adress=user.adress.first(),
                    total_price=0,
                    status=1
                )
                new_order.save()
                session = self.request.session
                session['order_id'] = new_order.pk
                #making book_in_order
                #bio - book in order
                for book_in_cart_id, bic_quantity in self.request.POST.items():
                    if book_in_cart_id not in ['csrfmiddlewaretoken', 'submit_button']:
                        book_in_cart = BookInCart.objects.get(pk=int(book_in_cart_id))
                        book_in_order = BookInOrder.objects.create(
                            order = new_order,
                            book = book_in_cart.book,       
                            price = book_in_cart.price,           
                            quantity = bic_quantity) 
                        book_in_order.save()
                cost = new_order.get_total_price()
                new_order.total_price = cost
                new_order.save()
                cart.delete()
                session['cart_id'] = None
                return reverse_lazy('orders:order-view')
        return reverse_lazy('orders:cart')

class OrderView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = '/cart'
    model=Order
    template_name='orders/order.html'

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
        # orders context include
        order_id = self.request.session.get('order_id')
        user = self.request.user            
        if order_id:
            order = Order.objects.filter(pk=order_id).last()
            context['order'] = order           
            context['user'] = user

        else:
            return reverse_lazy('orders:cart')
        return super().get_context_data(**context)
