from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Book
from .forms import CreateBookForm

# Create your views here.


def show_books(request):
    books = Book.objects.all()
    con = {'books_key':books}
    return render(
        request, 
        template_name='dbook/book_list.html', 
        context=con
    )

def show_one_book(request, pk):
    book_pk = pk
    book = Book.objects.get(pk=book_pk)
    form = CreateBookForm(instance=book)
    con = {'form':form, 'book_pk':book_pk}
    return render(request, template_name='dbook/book.html', context=con)

def delete_book(request, pk):
    book_pk = pk
    del_book = Book.objects.get(pk=book_pk)
    del_book.delete()
    return HttpResponseRedirect('/book')

def create_book_view(request):
    if request.method == 'POST':
        form = CreateBookForm(data=request.POST)
        if form.is_valid():
            form = CreateBookForm(request.POST)
            form.save()
            return HttpResponseRedirect('/book')
    else:
        form = CreateBookForm()
    return render(
        request, 
        template_name='dbook/book_create.html', 
        context={'form':form, 'header':'Создаем книгу'}
        )

def update_book_view(request, pk):
    if request.method == 'POST':
        form = CreateBookForm(data=request.POST)
        if form.is_valid():
            old_book = Book.objects.get(pk=pk)
            new_book = CreateBookForm(request.POST, instance=old_book)
            new_book.save()
            return HttpResponseRedirect('/book')
    else:
        old_book = Book.objects.get(pk=pk)
        form = CreateBookForm(instance=old_book)
    return render(
        request, 
        template_name='dbook/book_create.html', 
        context={'form':form, 'header':'Изменяем книгу'}
        )