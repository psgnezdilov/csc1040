from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("huycontact", views.contact, name="contact page"),
    path("books", views.library, name="all_books"),
]
