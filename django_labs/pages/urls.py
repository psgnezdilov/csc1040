from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("contact", views.contact, name="contact"),
    path("books", views.library, name="all_books"),
    path("books/search", views.book_search, name="book_search"),
    path("books/<int:id>/", views.book, name="book"),
]
