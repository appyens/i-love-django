# _*_ encoding utf-8 _*_

""" views for book app """

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib import messages

from .models import Author, Book
from .forms import BookForm


def book_home(request):
    recent = Book.objects.filter(is_active=True).order_by('-created_on')[:3]
    return render(request, 'book/home.html', {'recent': recent, 'total': Book.total_books()})


class BookHome(TemplateView):
    template_name = 'book/home.html'

    def get_context_data(self, **kwargs):
        context = super(BookHome, self).get_context_data(**kwargs)
        context['recent'] = Book.objects.filter(is_active=True).order_by('-created_on')[:3]
        context['total'] = Book.total_books()
        return context


# using model form
@require_http_methods(['GET', 'POST'])
def add_book(request, ):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()

            # no need in redirects
            # form = BookForm()
            # return render(request, 'book/add.html', {'form': form})
            request.session.get('success', "Book has been saved successfully")
            return redirect('book:book_detail', slug=book.slug)
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
        # getting book objects
        books = Book.objects.filter(is_active=True).order_by('title')
        return render(request, 'book/book_list.html', {'books': books})


class BookListView(ListView):
    model = Book
    context_object_name = 'books'


def book_detail(request, slug_field):
    if request.method == 'GET':
        book = Book.objects.get(slug=slug_field)
        msg = request.session.get('msg', None)
        if msg:
            messages.success(request, msg)
        related_books = Book.objects.filter(genre=book.genre).exclude(title=book.title)
        return render(request, 'book/detail.html', {'book': book, 'related': related_books})


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        book = self.object
        context['related'] = Book.objects.filter(genre=book.genre).exclude(title=book.title)
        context['success'] = self.request.session.get('success', None)
        print(context)
        return context


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


def book_by_author(request, author_id=None):
    author = Author.objects.get(pk=author_id)
    books = Book.objects.filter(authors__id=author_id)
    return render(request, 'book/book_list.html', {'books': books, 'author': author})
