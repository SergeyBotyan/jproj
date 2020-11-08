from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View

from .models import Book
from .forms import BookForm



class BookListView(ListView):
    model=Book
    paginate_by = 20
    template_name='dbook/book_list.html'

class Book5ListView(ListView):
    model=Book
    ordering='-pk'
    template_name='dbook/book_list.html'

    def get_queryset(self):
        return super().get_queryset()[0:5]


class BookDetailView(DetailView):
    model=Book
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        book =  Book.objects.get(pk=pk)
        context['form'] = BookForm(instance=book)
        return context
    
class BookCreateView(CreateView):
    model=Book
    fields='__all__'
    template_name = 'dbook/book_create.html'
    success_url = '/book'

class BookDeleteView(DeleteView):
    model=Book
    success_url = '/book'

class BookUpdateView(UpdateView):
    model=Book
    fields = '__all__'
    success_url = '/book'
    template_name = 'dbook/book_create.html'
    template_name_suffix = '_update_form'
