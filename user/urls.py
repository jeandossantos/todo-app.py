from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.create_user, name='create_user'),
    path('test/', views.authenticated, name='test'),
    path('logout/', views.logout_user, name='logout'),
]
