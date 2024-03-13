from django.urls import path

from . import views

urlpatterns = [
    path('', views.books_home, name='books-home'),
    path('authors/', views.authors_home, name='books-authors'),
    path('reading_list/', views.reading_list, name='books-reading-list'),
    path('reading_list/add/<int:pk>/', views.reading_list_add, name='books-reading-list-add'),
    path('reading_list/delete/<int:pk>/', views.reading_list_delete, name='books-reading-list-delete'),
]
