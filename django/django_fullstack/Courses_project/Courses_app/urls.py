from django.urls import path
from . import views

urlpatterns = [
    path('',views.main),
    path('create', views.create),
    path('courses/destroy/<int:id>', views.destroy),
    path('delete/<int:id>', views.delete),
    path('comment/<int:id>', views.comment),
    path('create_comment/<int:id>',views.create_comment)
]