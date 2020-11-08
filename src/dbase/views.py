from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Author, Book_series, Genre, Publisher
from .forms import AuthorForm, GenreForm, PublisherForm, SeriesForm
from dbook.models import Book
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View

# Create your views here.

class Select(ListView):
    model=Book
    ordering='-pk'
    template_name='dbase/select.html'

    def get_queryset(self):
        ordering='-pk'
        return super().get_queryset()[0:9]


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
    login_url = '/admin/login/'
    redirect_field_name = '/author'
    model=Author
    fields='__all__'
    template_name = 'dbase/create.html'
    success_url = '/book'

class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/admin/login/'
    redirect_field_name = '/author'
    model=Author
    success_url = '/author'

class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/admin/login/'
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
    login_url = '/admin/login/'
    redirect_field_name = '/series'
    model=Book_series
    fields='__all__'
    template_name = 'dbase/create.html'
    success_url = '/series'

class SeriesDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/admin/login/'
    redirect_field_name = '/series'
    model=Book_series
    success_url = '/series'

class SeriesUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/admin/login/'
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
    login_url = '/admin/login/'
    redirect_field_name = '/genre'
    model=Genre
    fields='__all__'
    template_name = 'dbase/create.html'
    success_url = '/genre'

class GenreDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/admin/login/'
    redirect_field_name = '/genre'
    model=Genre
    success_url = '/genre'

class GenreUpdateView(UpdateView):
    login_url = '/admin/login/'
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
    login_url = '/admin/login/'
    redirect_field_name = '/publisher'
    model=Publisher
    fields='__all__'
    template_name = 'dbase/create.html'
    success_url = '/publisher'

class PublisherDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/admin/login/'
    redirect_field_name = '/publisher'
    model=Publisher
    success_url = '/publisher'

class PublisherUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/admin/login/'
    redirect_field_name = '/publisher'
    model=Publisher
    fields = '__all__'
    success_url = '/publisher'
    template_name = 'dbase/create.html'
    template_name_suffix = '_update_form'