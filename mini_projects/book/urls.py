from django.urls import path
from .views import add_author, add_genre, add_language, add_book,\
    book_list, author_list, book_detail, edit_book, delete_book, book_home

urlpatterns = [
    path('home/', book_home, name='books_home'),
    path('list/', book_list, name='book_list'),
    path('list/authors/', author_list, name='authors_list'),
    path('<slug:slug_field>/', book_detail, name='book_detail'),

    # for vilas
    path('add/author/', add_author, name='add_author'),
    path('add/genre/', add_genre, name='add_genre'),
    path('add/language/', add_language, name='add_language'),
    path('add/', add_book, name='add_book'),
    path('edit/<int:book_id>/', edit_book, name='book_edit'),
    path('delete/<int:book_id>/', delete_book, name='delete_book'),
]
