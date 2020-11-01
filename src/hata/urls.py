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
from hello_world.views import hello_world
from dbase.views import select, show_authors, show_one_author, show_book_series, show_one_series
from dbase.views import show_genre, show_one_genre, show_publishers, show_one_publisher
from dbase.views import update_genre, delete_genre, create_genre
from dbase.views import update_book_series, delete_book_series, create_book_series
from dbase.views import update_publishers, delete_publishers, create_publishers
from dbase.views import update_authors, delete_authors, create_authors
from dbook.views import show_books, create_book_view, update_book_view, show_one_book, delete_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', show_books),
    path('book/<int:pk>/', show_one_book),
    path('book/create/', create_book_view),
    path('book/update/<int:pk>/', update_book_view),
    path('book/delete/<int:pk>/', delete_book),
    path('author/', show_authors),
    path('author/<int:pk>/', show_one_author),
    path('author/create/', create_authors),
    path('author/update/<int:pk>/', update_authors),
    path('author/delete/<int:pk>/', delete_authors),    
    path('series/', show_book_series),
    path('series/<int:pk>/', show_one_series),
    path('series/create/', create_book_series),
    path('series/update/<int:pk>/', update_book_series),
    path('series/delete/<int:pk>/', delete_book_series),
    path('genre/', show_genre),
    path('genre/<int:pk>/', show_one_genre),
    path('genre/create/', create_genre),
    path('genre/update/<int:pk>/', update_genre),
    path('genre/delete/<int:pk>/', delete_genre),
    path('publisher/', show_publishers),
    path('publisher/<int:pk>/', show_one_publisher),
    path('publisher/create/', create_publishers),
    path('publisher/update/<int:pk>/', update_publishers),
    path('publisher/delete/<int:pk>/', delete_publishers),
    path('', select)
]
