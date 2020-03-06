from django.shortcuts import render
from ..models import Book


def top(request):
    template_name = 'top.html'
    book_list = list(Book.objects.all().values())
    books = {'books': book_list}

    return render(request, template_name, books)
