from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page),
    path('process_1', views.process_one),
    path('process_2', views.process_two),
    path('delete/<int:id>', views.delete),
]