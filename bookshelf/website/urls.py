from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import api_endpoints, views

urlpatterns = [
                  path('', views.home, name='home'),
                  path('logout/', views.logout_user, name='logout'),
                  path('register/', views.register_user, name='register'),
                  path('book/<int:pk>', views.book, name='book'),
                  path('delete_book/<int:pk>', views.delete_book, name='delete_book'),
                  path('add_book/', views.add_book, name='add_book'),
                  path('add_author/', views.add_author, name='add_author'),
                  path('add_comment/<int:pk>', views.add_comment, name='add_comment'),
                  path('update_book/<int:pk>', views.update_book, name='update_book'),
                  path('books_list/', api_endpoints.books_list_api, name='books_list_api'),
                  path('books_list/<int:pk>', api_endpoints.book_api, name='book_api'),
                  path('search_books/', views.search_books, name='search_books'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
