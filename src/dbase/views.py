import requests
from requests.exceptions import ConnectionError
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Author, Book_series, Genre, Publisher
from .forms import AuthorForm, GenreForm, PublisherForm, SeriesForm
from dbook.models import Book
from orders.models import Order, BookInOrder, Cart
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View

# Create your views here.

class Select(LoginRequiredMixin, ListView):
    model=Book
    login_url = '/accounts/login/'
    ordering='-pk'
    template_name='dbase/select.html'

    def get_queryset(self):
        ordering='-pk'
        return super().get_queryset()[0:9]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        querry = Book.objects.all()
        books_number = Book.objects.all().count
        active_books_number = Book.objects.all().filter(active=True).count
        inactive_books_number = Book.objects.all().filter(active=False).count
        orders = Order.objects.all()
        formed_orders_count = Order.objects.filter(status = 1).count
        active_orders_count = Order.objects.filter(status__gt = 1, status__lt = 4).count
        finished_orders_count = Order.objects.filter(status = 4)
        price_sum = 0
        for book in querry:
            if book.price is not None:
                price_sum += book.price
            else:
                continue
                price_sum = 0
        available = 0
        for book in querry:
            if book.books_available is not None:
                available += book.books_available
            else:
                continue
        context['orders'] = orders
        context['formed_orders_count'] = formed_orders_count
        context['active_orders_count'] = active_orders_count
        context['finished_orders_count'] = finished_orders_count
        context['books_number'] = books_number
        context['active_books_number'] = active_books_number
        context['inactive_books_number'] = inactive_books_number
        context['price_sum'] = price_sum
        context['available'] = available
        return context

class Index_Page(ListView):
    model=Book
    ordering='-pk'
    template_name='index.html'

    def get_queryset(self):
        ordering='-pk'
        return super().get_queryset()[0:9]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            url = 'https://www.nbrb.by/api/exrates/rates/145'
            r = requests.get(url, timeout=1000)
            r = r.json()
            rate = r.get('Cur_OfficialRate')
        except ConnectionError:
            rate = "No connection"
        context['rate'] = rate
        genres = Genre.objects.all()
        context['genres'] = genres
        return context

class AuthorListView(ListView):
    model=Author
    paginate_by = 20
    template_name='dbase/author_list.html'

class AuthorDetailView(DetailView):
    model=Author
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        author =  Author.objects.get(pk=pk)
        context['form'] = AuthorForm(instance=author)
        return context
    
class AuthorCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = '/author'
    model=Author
    fields='__all__'
    template_name = 'dbase/create.html'
    success_url = '/book'

class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = '/author'
    model=Author
    success_url = '/author'

class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    redirect_field_name = '/author'
    model=Author
    fields = '__all__'
    success_url = '/author'
    template_name = 'dbase/create.html'
    template_name_suffix = '_update_form'

class SeriesListView(ListView):
    model=Book_series
    paginate_by = 20
    template_name='dbase/series_list.html'

class SeriesDetailView(DetailView):
    model=Book_series
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        series =  Book_series.objects.get(pk=pk)
        context['form'] = SeriesForm(instance=series)
        return context
    
class SeriesCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = '/series'
    model=Book_series
    fields='__all__'
    template_name = 'dbase/create.html'
    success_url = '/series'

class SeriesDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = '/series'
    model=Book_series
    success_url = '/series'

class SeriesUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission = 'dbase.change_book_series'
    login_url = '/accounts/login/'
    redirect_field_name = '/series'
    model=Book_series
    fields = '__all__'
    success_url = '/series'
    template_name = 'dbase/create.html'
    template_name_suffix = '_update_form'

class GenreListView(ListView):
    model=Genre
    paginate_by = 20
    template_name='dbase/genre_list.html'

class GenreDetailView(DetailView):
    model=Genre
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        genre =  Genre.objects.get(pk=pk)
        context['form'] = GenreForm(instance=genre)
        return context
    
class GenreCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = '/genre'
    model=Genre
    fields='__all__'
    template_name = 'dbase/create.html'
    success_url = '/genre'

class GenreDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = '/genre'
    model=Genre
    success_url = '/genre'

class GenreUpdateView(UpdateView):
    login_url = '/accounts/login/'
    redirect_field_name = '/genre'
    model=Genre
    fields = '__all__'
    success_url = '/genre'
    template_name = 'dbase/create.html'
    template_name_suffix = '_update_form'

class PublisherListView(ListView):
    model=Publisher
    paginate_by = 20
    template_name='dbase/publisher_list.html'

class PublisherDetailView(DetailView):
    model=Publisher
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        publisher =  Publisher.objects.get(pk=pk)
        context['form'] = PublisherForm(instance=publisher)
        return context
    
class PublisherCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = '/publisher'
    model=Publisher
    fields='__all__'
    template_name = 'dbase/create.html'
    success_url = '/publisher'

class PublisherDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = '/publisher'
    model=Publisher
    success_url = '/publisher'

class PublisherUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    redirect_field_name = '/publisher'
    model=Publisher
    fields = '__all__'
    success_url = '/publisher'
    template_name = 'dbase/create.html'
    template_name_suffix = '_update_form'