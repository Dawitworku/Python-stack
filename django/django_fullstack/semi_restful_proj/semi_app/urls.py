from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_shows),      # localhost:8000/shows
    path('new', views.new_show),    # localhost:8000/shows/new
    path('create_show', views.create_show),  # localhost:8000/shows/create_show
    path('<int:id>', views.show_shows),      # localhost:8000/shows/<int:id>
    path('<int:id>/edit', views.edit_show),  # localhost:8000/shows/<int:id>/edit
    path('<int:id>/update', views.update),   # localhost:8000/shows/<int:id>update
    path('<int:id>/destroy', views.destroy), # localhost:8000/shows/<int:id>destroy
]