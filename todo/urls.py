from django.urls import path

from . import views
urlpatterns = [
    path('view_todo/', views.view_todo, name='view_todo'),
    path('delete_todo/<int:id>', views.delete_todo, name='delete_todo'),
]
