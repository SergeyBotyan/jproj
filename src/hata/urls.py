"""hata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from hello_world.views import hello_world
from dbase.views import select, show_authors, show_one_author, show_book_series, show_one_series
from dbase.views import show_genre, show_one_genre, show_publishers, show_one_publisher
from dbase.views import update_genre, delete_genre, create_genre
from dbase.views import update_book_series, delete_book_series, create_book_series
from dbase.views import update_publishers, delete_publishers, create_publishers
from dbase.views import update_authors, delete_authors, create_authors
from dbook.views import BookListView, BookCreateView, Book5ListView, BookDetailView, BookDeleteView, BookUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', BookListView.as_view()),
    path('book5/', Book5ListView.as_view()),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-view'),
    path('book/create/', BookCreateView.as_view()),
    path('book/update/<int:pk>/', BookUpdateView.as_view()),
    path('book/delete/<int:pk>/', BookDeleteView.as_view()),
    path('author/', show_authors),
    path('author/<int:pk>/', show_one_author, name='author-view'),
    path('author/create/', create_authors),
    path('author/update/<int:pk>/', update_authors),
    path('author/delete/<int:pk>/', delete_authors),    
    path('series/', show_book_series),
    path('series/<int:pk>/', show_one_series, name='series-view'),
    path('series/create/', create_book_series),
    path('series/update/<int:pk>/', update_book_series),
    path('series/delete/<int:pk>/', delete_book_series),
    path('genre/', show_genre),
    path('genre/<int:pk>/', show_one_genre, name='genre-view'),
    path('genre/create/', create_genre),
    path('genre/update/<int:pk>/', update_genre),
    path('genre/delete/<int:pk>/', delete_genre),
    path('publisher/', show_publishers),
    path('publisher/<int:pk>/', show_one_publisher, name='publisher-view'),
    path('publisher/create/', create_publishers),
    path('publisher/update/<int:pk>/', update_publishers),
    path('publisher/delete/<int:pk>/', delete_publishers),
    path('', select)
]
