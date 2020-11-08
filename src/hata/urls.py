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
from dbase.views import Select
from dbase.views import PublisherListView,PublisherDeleteView, PublisherDetailView, PublisherCreateView, PublisherUpdateView
from dbase.views import SeriesListView, SeriesDeleteView, SeriesDetailView, SeriesCreateView, SeriesUpdateView
from dbase.views import GenreListView, GenreDeleteView, GenreDetailView, GenreCreateView, GenreUpdateView
from dbase.views import AuthorListView, AuthorDeleteView, AuthorDetailView, AuthorCreateView, AuthorUpdateView
from dbook.views import BookListView, BookCreateView, Book5ListView, BookDetailView, BookDeleteView, BookUpdateView
from user.views import Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', BookListView.as_view()),
    path('book5/', Book5ListView.as_view()),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-view'),
    path('book/create/', BookCreateView.as_view()),
    path('book/update/<int:pk>/', BookUpdateView.as_view()),
    path('book/delete/<int:pk>/', BookDeleteView.as_view()),
    path('author/', AuthorListView.as_view()),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author-view'),
    path('author/create/', AuthorCreateView.as_view()),
    path('author/update/<int:pk>/', AuthorUpdateView.as_view()),
    path('author/delete/<int:pk>/', AuthorDeleteView.as_view()),    
    path('series/', SeriesListView.as_view()),
    path('series/<int:pk>/', SeriesDetailView.as_view(), name='series-view'),
    path('series/create/', SeriesCreateView.as_view()),
    path('series/update/<int:pk>/', SeriesUpdateView.as_view()),
    path('series/delete/<int:pk>/', SeriesDeleteView.as_view()),
    path('genre/', GenreListView.as_view()),
    path('genre/<int:pk>/', GenreDetailView.as_view(), name='genre-view'),
    path('genre/create/', GenreCreateView.as_view()),
    path('genre/update/<int:pk>/', GenreUpdateView.as_view()),
    path('genre/delete/<int:pk>/', GenreDeleteView.as_view()),
    path('publisher/', PublisherListView.as_view()),
    path('publisher/<int:pk>/', PublisherDetailView.as_view(), name='publisher-view'),
    path('publisher/create/', PublisherCreateView.as_view()),
    path('publisher/update/<int:pk>/', PublisherUpdateView.as_view()),
    path('publisher/delete/<int:pk>/', PublisherDeleteView.as_view()),
    path('auth/login/', Login.as_view(), name='login'),
    path('', Select.as_view())
]
