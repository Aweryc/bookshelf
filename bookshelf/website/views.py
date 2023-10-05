from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import Author, Book, Comment


def home(request: Request) -> HttpResponse:
    books = Book.objects.all()
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
        return render(request, 'home.html', {'books': books})


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
            # messages.success(request, "You have been successfully registered!")
            return redirect('home')
    else:
        form = SignUpForm(request.POST)
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


def book(request: Request, pk) -> HttpResponse:
    if request.user.is_authenticated:
        book = Book.objects.get(id=pk)
        author = Author.objects.get(id=book.author_id)
        author_name = f'{author.last_name.title()} {author.first_name.capitalize()[0]}.'
        return render(request, 'book.html', {'book': book, 'author_name': author_name})
    else:
        messages.success(request, "You must be logged in to view this page.")
        return redirect('home')


def delete_record(request: Request, pk) -> HttpResponse:
    if request.user.is_authenticated:

        del_it = Book.objects.get(id=pk)
        del_it.delete()

        messages.success(request, f"Book # {pk} deleted successfully.")
    else:
        messages.success(request, "You must be logged in to delete this page.")

    return redirect('home')


def add_record(request: Request) -> HttpResponse:
    form = AddBookForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, f"Record created successfully.")
                return redirect('home')

        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to created new Book.")
        return redirect('home')


def update_record(request: Request, pk) -> HttpResponse:
    if request.user.is_authenticated:
        cur_record = Book.objects.get(id=pk)
        form = AddBookForm(request.POST or None, instance=cur_record)
        if form.is_valid():
            form.save()
            messages.success(request, f"Book # {pk} updated successfully!")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to update this page.")
        return redirect('home')
