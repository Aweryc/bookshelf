from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()  # day of birth
    bio = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Author {self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=250)
    author_id = models.BigIntegerField(null=False)
    released_at = models.DateField()  # day of release
    cover = models.ImageField(upload_to='images/')
    user_add_id = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Book {self.title}"


class Comment(models.Model):
    user_add_id = models.BigIntegerField()
    text = models.CharField(max_length=250)
    book_id = models.BigIntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Book {self.id}"
