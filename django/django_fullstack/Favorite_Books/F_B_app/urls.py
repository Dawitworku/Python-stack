from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('books', views.main_page),
    path('add_book', views.add_book),
    path('books/<int:id>', views.show_book),
    path('books/edit/<int:id>', views.edit_book),
    path('books/delete', views.delete_book),
    path('books/un_fav_book/<int:id>', views.unfav_book),
    path('books/add_fav_book/<int:id>', views.add_fav_book),
]