from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Author, Book, Language, Genre, Publisher
from .forms import AuthorForm, BookForm
from django.views.decorators.http import require_GET, require_POST, require_http_methods


def book_home(request):
    recent = Book.objects.filter(is_active=True).order_by('-created_on')[:3]
    return render(request, 'book/home.html', {'recent': recent, 'total': Book.total_books()})


# using model form
@require_http_methods(['GET', 'POST'])
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = BookForm()
        return render(request, 'book/add.html', {'form': form})
    else:
        form = BookForm()
        return render(request, 'book/add.html', {'form': form})


@require_GET
def author_list(request):
    if request.method == 'GET':
        all_authors = Author.objects.all
        context = {'authors': all_authors, }
        return render(request, 'book/author_list.html', context)
    return render(request, 'book/author_list.html')


@require_http_methods(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.filter(is_active=True)
        return render(request, 'book/list.html', {'books': books})


def book_detail(request, slug_field):
    if request.method == 'GET':
        book = Book.objects.get(slug=slug_field)
        related_books = Book.objects.filter(genre=book.genre).exclude(title=book.title)
        return render(request, 'book/detail.html', {'book': book, 'related': related_books})


@require_http_methods(['GET', 'POST'])
def edit_book(request, pk):
    # book = Book.objects.get(slug=book_slug)
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(instance=book, data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect(book.get_absolute_url())
    return render(request, 'book/edit.html', {'form': form})


@require_POST
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    # soft delete
    book.is_active = False
    book.save()
    # hard delete
    # book.delete()
    return redirect('book_list')


def search_book(request):
    if request.method == "GET":
        query = request.GET.get('query', None)
        # simple search with title only
        # books = Book.objects.filter(title__icontains=query)
        # advanced lookup with Q
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) |
            Q(authors__first_name__icontains=query) | Q(authors__last_name__icontains=query)
        ).distinct()
        return render(request, 'book/list.html', {'books': books, 'query': query})
