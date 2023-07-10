from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('register', views.create_user, name='create_user'),
    path('profile', views.update_profile, name='update_profile'),
    path('update_password', views.update_user_password, name='update_password'),
    path('logout', views.logout_user, name='logout'),
]
