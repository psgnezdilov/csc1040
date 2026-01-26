from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.
def index(request):
    username = request.GET.get("username", "Guest")
    return render(request, "index.html", {"username": username})


def contact(request):
    return render(request, "contact.html")

def library(request):
    books = Book.objects.all()
    return render(request, "books.html", {"all_books": books})

def book(request, id):
    book = get_object_or_404(Book,  id=id)
    return render(request, "book.html", {"book": book})

def book_search(request):
    query = request.GET.get("q", "")

    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.none()

    return render(request, 'book_search.html', {'books': books, 'query': query})