from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import AuthorSearchForm, BookSearchForm
from .models import Author, Book, ReadingList


@login_required
def books_home(request):
    keys = ('book_name', 'book_author', 'book_genre', 'book_popularity')
    if any(key in request.GET for key in keys):
        form = BookSearchForm(request.GET)

        if form.is_valid():
            name = form.cleaned_data.get('book_name')
            author = form.cleaned_data.get('book_author')
            genre = form.cleaned_data.get('book_genre')
            popularity = form.cleaned_data.get('book_popularity')

            if popularity is None:
                books = Book.objects.filter(title__icontains=name,
                                            author__icontains=author,
                                            genre__icontains=genre,)
            else:
                books = Book.objects.filter(title__icontains=name,
                                            author__icontains=author,
                                            genre__icontains=genre,
                                            popularity=popularity,)
            
            context = {
                'title': 'Book Catalogue',
                'max_popularity': 10,
                'books': books,
            }
    else:
        context = {
            'title': 'Book Catalogue',
            'max_popularity': 10,
            'books': Book.objects.all(),
            'authors': Author.objects.all(),
        }

    return render(request, 'books/books.html', context)


@login_required
def reading_list(request):
    books = (ReadingList.objects
             .filter(user=request.user)
             .first()
             .books.all())

    context = {
        'title': 'Reading List',
        'max_popularity': 10,
        'books': books,
    }
    return render(request, 'books/reading_list.html', context)


@login_required
def authors_home(request):
    if 'author_name' in request.GET:
        form = AuthorSearchForm(request.GET)

        if form.is_valid():
            name = form.cleaned_data.get('author_name')
            authors = Author.objects.filter(name__icontains=name)
            context = {
                'title': 'Book Catalogue',
                'authors': authors
            }
    else:
        context = {
            'title': 'Book Catalogue',
            'authors': Author.objects.all()
        }

    return render(request, 'books/authors.html', context)


def reading_list_add(request, pk):
    book = Book.objects.get(pk=pk)
    reading_list = ReadingList.objects.filter(user=request.user).first()
    reading_list.books.add(book)
    return redirect('books-home')


def reading_list_delete(request, pk):
    book = Book.objects.get(pk=pk)
    reading_list = ReadingList.objects.filter(user=request.user).first()
    reading_list.books.remove(book)
    return redirect('books-reading-list')