from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('home/', views.book_home, name='book_home'),
    path('list/', views.book_list, name='book_list'),
    path('list/authors/', views.author_list, name='authors_list'),
    path('add/', views.add_book, name='add_book'),
    path('<slug:slug_field>/', views.book_detail, name='book_detail'),
    # for vilas
    path('add/author/', views.add_author, name='add_author'),
    path('add/genre/', views.add_genre, name='add_genre'),
    path('add/language/', views.add_language, name='add_language'),
    path('edit/<int:book_id>/', views.edit_book, name='book_edit'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]
