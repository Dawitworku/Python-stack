from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('wall', views.wall_page),
    path('logout', views.logout),
    path('post_message', views.post_message),
    path('post_comment/<int:mess_id>', views.post_comment),
    path('wall/delete_message/<int:id>', views.delete_message),
    path('wall/delete_comment/<int:id>', views.delete_comment),
    path('wall/message_like/<int:id>', views.messages_likes),
    path('wall/message_unlike/<int:id>', views.messages_unlike),
]
