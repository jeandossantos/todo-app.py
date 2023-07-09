from django.urls import path

from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('delete_todo/<int:id>', views.delete_todo, name='delete_todo'),
    path('edit_todo/<int:id>', views.edit_todo, name='edit_todo'),
    path('toggle_todo_done/<int:id>',
         views.toggle_todo_done, name='toggle_todo_done'),
]
