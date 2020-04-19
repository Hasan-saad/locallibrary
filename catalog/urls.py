from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'), 
    path('cars/', views.BookListView.as_view(), name='cars'),
    path('car/<int:pk>', views.BookDetailView.as_view(),name='car-detail'),
    path('author/', views. AuthorListView.as_view(), name= 'authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(),name='author-detail'),
    path('create/', views.CreateBookView.as_view(), name='create_book'),
]