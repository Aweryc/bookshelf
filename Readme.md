## Bookshelf

It's a small project to store a books, authors and comments about books for registered users.
Also, you can search book on site.

#### Bookshelf API has some endpoints:

1. Get a list of all books: http://127.0.0.1:8000/book_list/
2. Get an info about one book:  http://127.0.0.1:8000/book_list/{book_id}.

   Where book_id: int

### How to start
1. To run a project please clone via git in a folder on your machine.
2. Set a virtual environment: python -m venv venv.
3. Install all requirements. `pip install -r requirements.txt`  .
4. Change directory to a <folder>/bookshelf: `cd .\bookshelf\`.
5. Run a `py.exe manage.py runserver`.
6. Sever should start, and now you can go ta site in a browser http://127.0.0.1:8000.
7. Now you can register and browse books.