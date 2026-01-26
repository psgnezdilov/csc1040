from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    return render(request, "index.html")


def contact(request):
    return render(request, "contact.html")

def libary(request):
    books = Books.objects.all()
    return render(request, "books.html", {all_books: books})
