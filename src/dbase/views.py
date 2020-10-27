from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book_series, Genre, Publisher

# Create your views here.

def select(request):
    return render(request, template_name='dbase/select.html')

def show_authors(request):
    authors = Author.objects.all()
    con = {'authors_key':authors}
    return render(request, template_name='dbase/author_list.html', context=con)

def show_one_author(request, pk):
    author = Author.objects.get(pk=pk)
    con = {'author_key':author}
    return render(request, template_name='dbase/author.html', context=con)

def show_book_series(request):
    book_series = Book_series.objects.all()
    con = {'book_series_key':book_series}
    return render(request, template_name='dbase/series_list.html', context=con)

def show_one_series(request, pk):
    series = Book_series.objects.get(pk=pk)
    con = {'series_key':series}
    return render(request, template_name='dbase/series.html', context=con)

def show_genre(request):
    genre = Genre.objects.all()
    con = {'genre_key':genre}
    return render(request, template_name='dbase/genre_list.html', context=con)

def show_one_genre(request, pk):
    genre = Genre.objects.get(pk=pk)
    con = {'genre_key':genre}
    return render(request, template_name='dbase/genre.html', context=con)

def show_publishers(request):
    pub = Publisher.objects.all()
    con = {'publisher_key':pub}
    return render(request, template_name='dbase/publisher_list.html', context=con)

def show_one_publisher(request, pk):
    pub = Publisher.objects.get(pk=pk)
    con = {'publisher_key':pub}
    return render(request, template_name='dbase/publisher.html', context=con)
