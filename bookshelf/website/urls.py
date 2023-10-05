from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('book/<int:pk>', views.book, name='book'),
    path('delete/<int:pk>', views.delete_record, name='delete_book'),
    path('add_book/', views.add_record, name='add_book'),
    path('update/<int:pk>', views.update_record, name='update_book'),
]
