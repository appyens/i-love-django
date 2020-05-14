from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('home/', views.book_home, name='book_home'),
    path('list/', views.book_list, name='book_list'),
    path('list/authors/', views.author_list, name='authors_list'),
    path('add/', views.add_book, name='add_book'),
    path('search_book/', views.search_book, name='search_book'),
    path('<slug:slug_field>/', views.book_detail, name='book_detail'),
    # for vilas
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]
