from django.contrib import admin
from .models import Author, Comment, Book


admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Book)