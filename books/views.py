from django.shortcuts import render
from books.models import Book


def books_view(request, pub_date=None):
    template = 'books/books_list.html'

    if pub_date:
        books_list = list(Book.objects.filter(pub_date=pub_date))
        context = {'books': books_list,
                   'pub_date': pub_date}
    else:

        books_list = list(Book.objects.all())
        # for book in books_list:
        #     print(book.pub_date)
        context = {'books': books_list}
    return render(request, template, context)
