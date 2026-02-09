from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from .models import *
from .forms import BookForm, AuthorForm


# Create your views here.
def index(request):
    username = request.GET.get("username", "Guest")
    return render(request, "index.html", {"username": username})

def authors(request):
    authors = Author.objects.all()
    return render(request, "authors.html", {"authors":authors})

@login_required
@user_passes_test(lambda u: u.is_staff)
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_authors')
    else:
        form = AuthorForm()
    return render(request, "add_author.html", {"form":form})


def contact(request):
    return render(request, "contact.html")

def library(request):
    author = request.GET.get("author", "")
    title = request.GET.get("title", "")
    if author and title:
        books = Book.objects.filter(title__icontains=title, author__name=author)
    else:
        books = Book.objects.all()
    return render(request, "books.html", {"all_books": books, "author":author, "title":title})

def book(request, id):
    book = get_object_or_404(Book,  id=id)
    return render(request, "book.html", {"book": book})

def books_year(request, year):
    books = Book.objects.filter(year__icontains=year)
    return render(request, 'books_year.html', {'books': books, 'year': year})

def books_category_year(request, year, category):
    books = Book.objects.filter(year__icontains=year, category=category)
    return render(request, 'books.html', {'all_books': books})

@login_required
@user_passes_test(lambda u: u.is_staff)
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
    return render(request, 'add_book.html', {'form':form})

def edit_book(request, bookid):
    book = get_object_or_404(Book, id=bookid)

    if not request.user.is_staff and book.added_by != request.user:
        return HttpResponseForbidden("You can only edit books you added.")

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book', id=book.id)
    else:
        form = BookForm(instance=book)

    return render(request, 'edit_book.html', {'form':form, 'book':book})

def delete_book(request, bookid):
    book = get_object_or_404(Book, id=bookid)

    if not request.user.is_staff and request.user != book.added_by:
        return HttpResponseForbidden("You can only delete books you added.")

    if request.method == "POST":
        book.delete()
        return redirect('all_books')

    return render(request, 'confirm_delete.html', {'book':book})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form":form})

@login_required
def profile(request):
    return render(request, 'profile.html')