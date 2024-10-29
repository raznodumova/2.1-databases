from datetime import datetime, timedelta

from django.core.paginator import Paginator
from django.db.models import Min, Max
from django.shortcuts import render
from .models import Book


def books_view(request):
    template = 'books/books_list.html'

    books = Book.objects.all().order_by('pub_date')

    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, template, context)


def get_books_for_date(date):
    return Book.objects.filter(pub_date=date).order_by('pub_date')


def books_by_date_view(request, pub_date):
    template = 'books/books_list.html'

    date = datetime.strptime(pub_date, '%Y-%m-%d').date()

    books = get_books_for_date(date)

    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    previous_date = date - timedelta(days=1)
    next_date = date + timedelta(days=1)

    while previous_date >= Book.objects.aggregate(Min('pub_date'))['pub_date__min']:
        if get_books_for_date(previous_date).exists():
            break
        previous_date -= timedelta(days=1)

    while next_date <= Book.objects.aggregate(Max('pub_date'))['pub_date__max']:
        if get_books_for_date(next_date).exists():
            break
        next_date += timedelta(days=1)

    context = {
        'page_obj': page_obj,
        'previous_date': previous_date,
        'next_date': next_date,
    }

    return render(request, template, context)