from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("contact", views.contact, name="contact"),
    path("books", views.library, name="all_books"),
    path("books/search", views.book_search, name="book_search"),
    path("books/add", views.add_book, name="add_book"),
    path("books/<int:id>/", views.book, name="book"),
    path("books/year/<int:year>/", views.books_year, name="books_year"),
    path("books/category/<str:category>/year/<int:year>/", views.books_category_year, name="book_category_year"),
    path("register/", views.register, name="register")
]
