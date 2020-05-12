from django.shortcuts import render, redirect
from common.utils import slug_generator
from .models import Author, Book, Language, Genre, Publisher
from .forms import AddAuthorForm, AddBookForm

# Create your views here.


def book_home(request):
    recent = Book.objects.filter(is_active=True).order_by('-created_on')[:3]
    return render(request, 'book/home.html', {'recent': recent, 'total': Book.total_books()})


# def add_author(request):
#     if request.method == 'POST':
#         data = request.POST
#         first_name = data['first_name']
#         last_name = data['last_name']
#         Author.objects.create(first_name=first_name, last_name=last_name)
#         return render(request, 'book/add_author.html', {})
#     return render(request, 'book/add_author.html')

def add_author(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            first_name = cd['first_name']
            last_name = cd['last_name']
            email = cd['email']
            dob = cd['dob']
            death = cd['death']
            Author.objects.create(first_name=first_name, last_name=last_name, dob=dob, death=death)
            form = AddAuthorForm()
            return render(request, 'book/add_author.html', {'form': form})
    else:
        form = AddAuthorForm()
        return render(request, 'book/add_author.html', {'form': form})


def add_language(request):
    if request.method == 'POST':
        data = request.POST
        lang = data['lang']
        Language.objects.create(language=lang)
        return render(request, 'book/add_language.html', {})
    return render(request, 'book/add_language.html')


def add_genre(request):
    if request.method == 'POST':
        data = request.POST
        genre = data['genre']
        Genre.objects.create(genre=genre)
        return render(request, 'book/add_genre.html', {})
    return render(request, 'book/add_genre.html')


def add_book(request):
    all_authors = Author.objects.all()
    all_langs = Language.objects.all()
    all_genre = Genre.objects.all()

    # taking from user
    if request.method == 'POST':
        data = request.POST
        title = data['title']
        pages = data['pages']
        language_id = data['lang']
        desc = data['desc']
        genre_id = data['genre']
        author_id = data['author']
        year = data['year']
        pub = data['pub']

        # getting object from db
        author = Author.objects.get(id=author_id)
        language = Language.objects.get(id=language_id)
        genre = Genre.objects.get(id=genre_id)

        # getting files
        front_cover = request.FILES.get('f_cover', None)
        back_cover = request.FILES.get('b_cover', None)

        # assigning to the model
        book = Book.objects.create(
            title=title,
            slug=slug_generator(title),
            pages=pages,
            language=language,
            description=desc,
            genre=genre,
            year=year,
            publication=pub,
            front_cover=front_cover,
            back_cover=back_cover
        )
        book.authors.add(author)
        book.save()
        return render(request, 'book/add.html',)

    context = {'authors': all_authors,
               'languages': all_langs, 'genres': all_genre}
    return render(request, 'book/add.html', context)


def author_list(request):
    if request.method == 'GET':
        all_authors = Author.objects.all
        context = {'authors': all_authors, }
        return render(request, 'book/author_list.html', context)
    return render(request, 'book/author_list.html')


def book_list(request):
    if request.method == 'GET':
        books = Book.objects.filter(is_active=True)
        context = {'books': books}
        return render(request, 'book/list.html', context)
    return render(request, 'book/list.html', context)


def book_detail(request, slug_field):
    if request.method == 'GET':
        book = Book.objects.get(slug=slug_field)
        return render(request, 'book/detail.html', {'book': book})


def edit_book(request, book_id=None):
    book = Book.objects.get(id=book_id)
    all_authors = Author.objects.all()
    all_genre = Genre.objects.all()
    all_langs = Language.objects.all()
    if request.method == 'POST':
        data = request.POST
        title = data['title']
        pages = data['pages']
        language_id = data['lang']
        desc = data['desc']
        genre_id = data['genre']
        author_id = data['author']
        year = data['year']
        pub = data['pub']
        author = Author.objects.get(id=author_id)
        language = Language.objects.get(id=language_id)
        genre = Genre.objects.get(id=genre_id)
        book.title = title
        book.pages = pages
        book.description = desc
        book.year = year
        book.publication = pub
        book.language = language
        book.genre = genre
        book.author = author
        book.save()
        return redirect(book.get_absolute_url())
    return render(request, 'book/edit.html', {'book': book, 'authors': all_authors,
                                                   'languages': all_langs, 'genres': all_genre})


def delete_book(request, book_id):

    book = Book.objects.get(id=book_id)
    book.is_active = False
    book.save()
    # hard delete
    # book.delete()
    return redirect('book_list')
