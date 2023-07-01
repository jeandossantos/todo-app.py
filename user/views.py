from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password as encrypt_password
from django.contrib.auth.hashers import check_password as verify_password
from django.contrib.auth import login, authenticate, logout

# from .models import User
from .forms import RegisterForm, LoginForm


def create_user(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        email = request.POST.get('email')

        if _user_exists(email):
            return render(request, 'register.html', {
                'form': {
                    'errors': {
                        'email': 'Please enter a valid email address'
                    }
                }
            })

        if form.is_valid():
            _create_new_user(request)

            return redirect('/users/login')
        else:
            return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    errors = {
        'errors': {
            'email': 'invalid credentials',
            'password': 'invalid credentials'
        }
    }

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            authenticated_user = authenticate(
                request, email=email, password=password
            )
            print(authenticated_user)
            if authenticated_user is not None:
                login(request, authenticated_user)

                return redirect('/users/test')
            else:
                return render(request, 'login.html', {'form': errors})
        else:
            return render(request, 'login.html', {'form': errors})


def logout_user(request):
    logout(request)

    return redirect('/users/login')


def authenticated(request):
    return render(request, 'test.html')


def _user_exists(email):
    return User.objects.filter(email=email).exists()


def _create_new_user(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = User()
    user.name = name
    user.email = email
    user.password = encrypt_password(password)

    user.save()
