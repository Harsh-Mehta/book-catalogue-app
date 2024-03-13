from django.contrib import admin

from .models import Author, Book, ReadingList

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(ReadingList)