from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page),
    path('books', views.books),
    path('authors', views.authors),
    path('authors_page', views.authors_page),
    path('books/<int:id>', views.view_book),
    path('authors/<int:id>', views.view_author),
    path('assign_author/<int:id>',views.author_form),
    path('assign_book/<int:id>', views.book_form),
]
