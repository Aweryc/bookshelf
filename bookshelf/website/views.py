from typing import Optional
from urllib.request import Request

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import Author, Book, Comment
from django.core.paginator import Paginator


def home(request: Request) -> HttpResponse:
    books = Book.objects.all()
    books_paginator = Paginator(books, 2)
    page = request.GET.get('page')
    paged_books = books_paginator.get_page(page)
    # Check if user logging in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "Something went wrong. Try again latter.")
            return redirect('home')
    else:
        return render(request, 'home.html', {'books': paged_books})


# def login_user(request):
#     pass


def logout_user(request: Request) -> HttpResponse:
    logout(request)
    messages.success(request, 'You have been logged out...')
    return redirect('home')


def register_user(request: Request) -> HttpResponse:
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm(request.POST)
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


def book(request: Request, pk) -> HttpResponse:
    if request.user.is_authenticated:
        return render_a_book(request, pk)
    else:
        messages.success(request, "You must be logged in to view this page.")
        return redirect('home')


def delete_book(request: Request, pk) -> HttpResponse:
    if request.user.is_authenticated:

        del_it = Book.objects.get(id=pk)
        del_it.delete()

        messages.success(request, f"Book # {pk} deleted successfully.")
    else:
        messages.success(request, "You must be logged in to delete this page.")

    return redirect('home')


def add_book(request: Request) -> HttpResponse:
    if request.user.is_authenticated:
        form = AddBookForm(request.POST or None, request.FILES)
        if request.method == "POST":
            if form.is_valid():
                temp_form = form.save(commit=False)
                temp_form.user_add = request.user
                temp_form.save()
                messages.success(request, f"Book added successfully!")
                return redirect('home')

        return render(request, 'add_book.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to created new Book.")
        return redirect('home')


def update_book(request: Request, pk) -> HttpResponse:
    if request.user.is_authenticated:
        cur_record = Book.objects.get(id=pk)
        form = AddBookForm(request.POST or None, instance=cur_record)
        if request.method == "POST":
            if request.FILES:
                form = AddBookForm(request.POST or None, request.FILES)
            else:
                form = AddBookForm(request.POST or None, instance=cur_record)
            if form.is_valid():
                temp_form = form.save(commit=False)
                temp_form.user_add = request.user
                temp_form.save()
                messages.success(request, f"Book # {pk} updated successfully!")
                return render_a_book(request, pk)

        return render(request, 'update_book.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to update this page.")
        return render_a_book(request, pk)


def search_books(request: Request) -> HttpResponse:
    if request.method == "POST":
        query = request.POST['query']
        if query:
            results = Book.objects.filter(Q(title__contains=query) | Q(desc__contains=query))
        else:
            results = None
        return render(request, 'search_books.html', {'results': results, 'query': query})
    else:
        return render(request, 'search_books.html', {})


def add_author(request: Request) -> HttpResponse:
    if request.user.is_authenticated:
        form = AddAuthorForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                temp_form = form.save(commit=False)
                temp_form.user_add = request.user
                temp_form.save()
                messages.success(request, f"Author added successfully.")
                return redirect('home')

        return render(request, 'add_author.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to created new Book.")
        return redirect('home')


def add_comment(request: Request, pk) -> HttpResponse:
    if request.user.is_authenticated:
        if request.method == "POST":
            comment = Comment()
            comment.user_add = request.user
            comment.book = Book.objects.get(pk=pk)
            if not request.POST['comment']:
                return render_a_book(request, pk)

            comment.text = request.POST['comment']

            comment.save()
            messages.success(request, f"Comment added successfully.")

            return render_a_book(request, pk)

        # elif request.method == "GET":
        #
        #     book: Book = Book.objects.get(id=pk)
        #     author = Author.objects.get(id=book.author.id)
        #     author_name = f'{author.last_name.title()} {author.first_name.capitalize()[0]}.'
        #     comments = Comment.objects.filter(book_id=pk)
        #
        #     return render(request, 'book.html', {'book': book, 'author_name': author_name, 'comments': comments})


def render_a_book(request: Request, pk) -> HttpResponse:
    """    Rendering a book page with a comments
    :type pk: Book id
    :type request: Request from client
    """
    book = Book.objects.get(id=pk)
    author = Author.objects.get(id=book.author.id)
    author_name = f'{author.last_name.title()} {author.first_name.capitalize()[0]}.'
    comments = Comment.objects.filter(book_id=pk)

    return render(request, 'book.html', {'book': book, 'author_name': author_name, 'comments': comments})
