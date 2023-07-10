from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('register', views.create_user, name='create_user'),
    path('profile', views.update_profile, name='update_profile'),
    path('logout', views.logout_user, name='logout'),
]
