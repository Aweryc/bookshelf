from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()  # day of birth
    bio = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    user_add = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    released_at = models.IntegerField()  # day of release
    desc = models.CharField(max_length=500)
    cover = models.ImageField(upload_to='images/')
    user_add = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Book {self.title}"


class Comment(models.Model):
    user_add = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    text = models.CharField(max_length=500)
    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment {self.id}"
