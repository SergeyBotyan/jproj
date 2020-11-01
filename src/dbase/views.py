from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Author, Book_series, Genre, Publisher
from .forms import CreateAuthorForm, CreateGenreForm, CreatePublisherForm, CreateSeriesForm

# Create your views here.

def select(request):
    return render(request, template_name='dbase/select.html')

def show_authors(request):
    authors = Author.objects.all()
    con = {'authors_key':authors}
    return render(request, template_name='dbase/author_list.html', context=con)

def show_one_author(request, pk):
    author_pk = pk
    author = Author.objects.get(pk=author_pk)
    con = {'author_key':author, 'author_pk':author_pk}
    return render(request, 
    template_name='dbase/author.html', 
    context=con)

def create_authors(request):
    if request.method == 'POST':
        form = CreateAuthorForm(data=request.POST)
        if form.is_valid():
            form = CreateAuthorForm(request.POST)
            form.save()
            return HttpResponseRedirect('/author')
    else:
        form = CreateAuthorForm()
    return render(request,
        template_name='dbase/create.html',
        context={'form':form, 'header':'Создаем автора'}
        )

def update_authors(request, pk):
    if request.method == 'POST':
        form = CreateAuthorForm(data=request.POST)
        if form.is_valid():
            old_author = Author.objects.get(pk=pk)
            new_author = CreateAuthorForm(request.POST, instance=old_author)
            new_author.save()
            return HttpResponseRedirect('/author')
    else:
        old_author = Author.objects.get(pk=pk)
        form = CreateAuthorForm(instance=old_author)
    return render(
        request, 
        template_name='dbase/create.html', 
        context={'form':form, 'header':'Изменяем автора'}
        )

def delete_authors(request, pk):
    author_pk = pk
    del_author = Author.objects.get(pk=author_pk)
    del_author.delete()
    return HttpResponseRedirect('/author')

def show_book_series(request):
    book_series = Book_series.objects.all()
    con = {'book_series_key':book_series}
    return render(request, template_name='dbase/series_list.html', context=con)

def show_one_series(request, pk):
    series_pk = pk
    series = Book_series.objects.get(pk=series_pk)
    con = {'series_key':series, 'series_pk':series_pk}
    return render(request, template_name='dbase/series.html', context=con)

def create_book_series(request):
    if request.method == 'POST':
        form = CreateSeriesForm(data=request.POST)
        if form.is_valid():
            form = CreateSeriesForm(request.POST)
            form.save()
            return HttpResponseRedirect('/series')
    else:
        form = CreateSeriesForm()
    return render(request,
        template_name='dbase/create.html',
        context={'form':form, 'header':'Создаем книжную серию'}
        )

def update_book_series(request, pk):
    if request.method == 'POST':
        form = CreateSeriesForm(data=request.POST)
        if form.is_valid():
            old_series = Book_series.objects.get(pk=pk)
            new_series = CreateSeriesForm(request.POST, instance=old_series)
            new_series.save()
            return HttpResponseRedirect('/series')
    else:
        old_series = Book_series.objects.get(pk=pk)
        form = CreateSeriesForm(instance=old_series)
    return render(
        request, 
        template_name='dbase/create.html', 
        context={'form':form, 'header':'Изменяем книжную серию'}
        )

def delete_book_series(request, pk):
    series_pk = pk
    del_series = Book_series.objects.get(pk=series_pk)
    del_series.delete()
    return HttpResponseRedirect('/series')

def show_genre(request):
    genre = Genre.objects.all()
    con = {'genre_key':genre}
    return render(request, template_name='dbase/genre_list.html', context=con)

def show_one_genre(request, pk):
    genre_pk = pk
    genre = Genre.objects.get(pk=genre_pk)
    con = {'genre_key':genre, 'genre_pk':genre_pk}
    return render(request, template_name='dbase/genre.html', context=con)

def create_genre(request):
    if request.method == 'POST':
        form = CreateGenreForm(data=request.POST)
        if form.is_valid():
            form = CreateGenreForm(request.POST)
            form.save()
            return HttpResponseRedirect('/genre')
    else:
        form = CreateGenreForm()
    return render(request,
        template_name='dbase/create.html',
        context={'form':form, 'header':'Создаем жанр'}
        )

def update_genre(request, pk):
    if request.method == 'POST':
        form = CreateGenreForm(data=request.POST)
        if form.is_valid():
            old_genre = Genre.objects.get(pk=pk)
            new_genre = CreateGenreForm(request.POST, instance=old_genre)
            new_genre.save()
            return HttpResponseRedirect('/genre')
    else:
        old_genre = Genre.objects.get(pk=pk)
        form = CreateGenreForm(instance=old_genre)
    return render(
        request, 
        template_name='dbase/create.html', 
        context={'form':form, 'header':'Изменяем жанр'}
        )

def delete_genre(request, pk):
    genre_pk = pk
    del_genre = Genre.objects.get(pk=genre_pk)
    del_genre.delete()
    return HttpResponseRedirect('/genre')

def show_publishers(request):
    pub = Publisher.objects.all()
    con = {'publisher_key':pub}
    return render(request, template_name='dbase/publisher_list.html', context=con)

def show_one_publisher(request, pk):
    publisher_pk = pk
    pub = Publisher.objects.get(pk=publisher_pk)
    con = {'publisher_key':pub, 'publisher_pk':publisher_pk}
    return render(request, template_name='dbase/publisher.html', context=con)

def create_publishers(request):
    if request.method == 'POST':
        form = CreatePublisherForm(data=request.POST)
        if form.is_valid():
            form = CreatePublisherForm(request.POST)
            form.save()
            return HttpResponseRedirect('/publisher')
    else:
        form = CreatePublisherForm()
    return render(request,
        template_name='dbase/create.html',
        context={'form':form, 'header':'Создаем издателя'}
        )

def update_publishers(request, pk):
    if request.method == 'POST':
        form = CreatePublisherForm(data=request.POST)
        if form.is_valid():
            old_publisher = Publisher.objects.get(pk=pk)
            new_publisher = CreatePublisherForm(request.POST, instance=old_publisher)
            new_publisher.save()
            return HttpResponseRedirect('/publisher')
    else:
        old_publisher = Publisher.objects.get(pk=pk)
        form = CreatePublisherForm(instance=old_publisher)
    return render(
        request, 
        template_name='dbase/create.html', 
        context={'form':form, 'header':'Изменяем издателя'}
        )

def delete_publishers(request, pk):
    publisher_pk = pk
    del_publisher = Publisher.objects.get(pk=publisher_pk)
    del_publisher.delete()
    return HttpResponseRedirect('/publisher')
