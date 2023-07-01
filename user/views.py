from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from .forms import RegisterForm, LoginForm


def create_user(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    form = RegisterForm(request.POST)

    if not form.is_valid():
        return render(request, 'register.html', {
            'form': {
                'errors': {
                    'username': 'Please enter a valid username'
                }
            }
        })

    username = form.cleaned_data["username"]

    if not _user_exists(username):
        _create_new_user(form)

        return redirect('/auth/login')


def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    errors = {
        'errors': {
            'email': 'invalid credentials',
            'password': 'invalid credentials'
        }
    }

    form = LoginForm(request.POST)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        authenticated_user = authenticate(
            request, username=username, password=password
        )

        if authenticated_user is not None:
            login(request, authenticated_user)

            return redirect('/auth/test')
        else:
            return render(request, 'login.html', {'form': errors})


def logout_user(request):
    logout(request)

    return redirect('/auth/login')


def _user_exists(username):
    return User.objects.filter(username=username).exists()


def _create_new_user(form):
    username = form.cleaned_data['username']
    email = form.cleaned_data['email']
    password = form.cleaned_data['password']

    user = User.objects.create_user(
        username=username, email=email, password=password
    )
    user.save()
