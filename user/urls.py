from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.create_user, name='create_user')
]
