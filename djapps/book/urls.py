from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('<int:pk>/edit/', views.edit_book, name='edit_book'),
    # path('home/', views.book_home, name='book_home'),
    path('home/', views.BookHome.as_view(), name='book_home'),
    path('list/', views.book_list, name='book_list'),
    # path('list/', views.BookListView.as_view(), name='book_list'),
    path('list/authors/', views.author_list, name='authors_list'),
    path('add/', views.add_book, name='add_book'),
    path('search_book/', views.search_book, name='search_book'),
    # path('<slug:slug_field>/', views.book_detail, name='book_detail'),
    path('<slug:slug>/', views.BookDetailView.as_view(), name='book_detail'),
    # for vilas

    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('author/<int:author_id>/', views.book_by_author, name='by_author'),
]
