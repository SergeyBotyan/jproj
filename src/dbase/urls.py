from django.conf.urls.static import static
from django.conf import settings
from django.urls import path


from dbase.views import Select, Index_Page
from dbase.views import PublisherListView,PublisherDeleteView, PublisherDetailView, PublisherCreateView, PublisherUpdateView
from dbase.views import SeriesListView, SeriesDeleteView, SeriesDetailView, SeriesCreateView, SeriesUpdateView
from dbase.views import GenreListView, GenreDeleteView, GenreDetailView, GenreCreateView, GenreUpdateView
from dbase.views import AuthorListView, AuthorDeleteView, AuthorDetailView, AuthorCreateView, AuthorUpdateView


app_name = 'dbase'

urlpatterns = [
    #path('delete-book-in-cart/<int:pk>', DeleteBookInCart.as_view(), name='delete-book-in-cart'),
    #path('update-cart', UpdateCart.as_view(), name='update-cart'),
   # path('', CartView.as_view(), name='cart'),
    path('author/', AuthorListView.as_view(), name='author-list'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('author/create/', AuthorCreateView.as_view(), name='author-create'),
    path('author/update/<int:pk>/', AuthorUpdateView.as_view(), name='author-update'),
    path('author/delete/<int:pk>/', AuthorDeleteView.as_view(), name='author-delete'),    
    path('series/', SeriesListView.as_view(), name='series-list'),
    path('series/<int:pk>/', SeriesDetailView.as_view(), name='series-detail'),
    path('series/create/', SeriesCreateView.as_view(), name='series-create'),
    path('series/update/<int:pk>/', SeriesUpdateView.as_view(), name='series-update'),
    path('series/delete/<int:pk>/', SeriesDeleteView.as_view(), name='series-delete'),
    path('genre/', GenreListView.as_view(), name='genre-list'),
    path('genre/<int:pk>/', GenreDetailView.as_view(), name='genre-detail'),
    path('genre/create/', GenreCreateView.as_view(), name='genre-create'),
    path('genre/update/<int:pk>/', GenreUpdateView.as_view(), name='genre-update'),
    path('genre/delete/<int:pk>/', GenreDeleteView.as_view(), name='genre-delete'),
    path('publisher/', PublisherListView.as_view(), name='publisher-list'),
    path('publisher/<int:pk>/', PublisherDetailView.as_view(), name='publisher-detail'),
    path('publisher/create/', PublisherCreateView.as_view(), name='publisher-create'),
    path('publisher/update/<int:pk>/', PublisherUpdateView.as_view(), name='publisher-update'),
    path('publisher/delete/<int:pk>/', PublisherDeleteView.as_view(), name='publisher-delete'),
]