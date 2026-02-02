from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import BookForm


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

def books_year(request, year):
    books = Book.objects.filter(year__icontains=year)
    return render(request, 'books_year.html', {'books': books, 'year': year})

def books_category_year(request, year, category):
    books = Book.objects.filter(year__icontains=year, category=category)
    return render(request, 'books.html', {'all_books': books})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.added_by = request.user
            book.save()
            return redirect('all_books')
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})