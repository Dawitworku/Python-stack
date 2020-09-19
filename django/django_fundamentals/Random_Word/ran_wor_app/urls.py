from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page),# or i can just do (views.random_word) to 
    path('random_word', views.random_word), #redirect the landing page to index.html
    path('reset', views.reset),
]

