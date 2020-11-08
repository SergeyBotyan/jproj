from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View

from .models import Book
from .forms import BookForm



class BookListView(ListView):
    model=Book
    paginate_by = 20
    template_name='dbook/book_list.html'

class BookDetailView(DetailView):
    model=Book
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        book =  Book.objects.get(pk=pk)
        context['form'] = BookForm(instance=book)
        return context
    
class BookCreateView(LoginRequiredMixin, CreateView):
    login_url = '/admin/login/'
    redirect_field_name = '/book'
    model=Book
    fields='__all__'
    template_name = 'dbook/book_create.html'
    success_url = '/book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        return context

class BookDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/admin/login/'
    redirect_field_name = '/book'
    model=Book
    success_url = '/book'

class BookUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/admin/login/'
    redirect_field_name = '/'
    model=Book
    fields = '__all__'
    success_url = '/book'
    template_name = 'dbook/book_create.html'
    template_name_suffix = '_update_form'

