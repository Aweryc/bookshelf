from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()  # day of birth
    bio = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    # author_id = models.IntegerField(null=True)
    released_at = models.IntegerField()  # day of release
    user_add_id = models.BigIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Book {self.title}"


class Comment(models.Model):
    user_add_id = models.BigIntegerField()
    text = models.CharField(max_length=250)
    book_id = models.BigIntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Book {self.id}"
