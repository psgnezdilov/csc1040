from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("contact", views.contact, name="contact"),
    path("books", views.library, name="all_books"),
    path("books/add", views.add_book, name="add_book"),
    path("books/<int:id>/", views.book, name="book"),
    path("books/<int:bookid>/edit", views.edit_book, name="edit_book"),
    path("books/<int:bookid>/delete", views.delete_book, name="delete_book"),
    path("books/year/<int:year>/", views.books_year, name="books_year"),
    path("books/category/<str:category>/year/<int:year>/", views.books_category_year, name="book_category_year"),
    path("authors/", views.authors, name="all_authors"),
    path("authors/add", views.add_author, name="add_author"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
]
