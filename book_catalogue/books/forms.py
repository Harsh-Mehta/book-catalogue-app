from django import forms


class BookSearchForm(forms.Form):
    book_name = forms.CharField(label="book_name", max_length=200, required=False)
    book_author = forms.CharField(label="book_author", max_length=200, required=False)
    book_genre = forms.CharField(label="book_genre", max_length=200, required=False)
    book_popularity = forms.IntegerField(label="book_popularity", required=False)


class AuthorSearchForm(forms.Form):
    author_name = forms.CharField(label="author_name", max_length=200)