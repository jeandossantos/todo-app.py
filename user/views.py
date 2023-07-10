from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
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
        username = form.cleaned_data['username'].lower()
        password = form.cleaned_data['password']

        authenticated_user = authenticate(
            request, username=username, password=password
        )

        if authenticated_user is not None:
            login(request, authenticated_user)
            request.session['user_id'] = authenticated_user.id

            return redirect('/todo/home/')
        else:
            return render(request, 'login.html', {'form': errors})


def logout_user(request):
    logout(request)

    return redirect('/auth/login')


def update_profile(request):
    if request.method == 'GET':
        return render(request, 'profile.html')

    username = request.POST.get('username')

    if request.user.username == username:
        return render(request, 'profile.html', {
            'errors': {
                'username': 'Já está em uso.'
            }
        })

    if len(username.strip()) < 2:
        return render(request, 'profile.html', {
            'errors': {
                'username': 'Muito curto!'
            }
        })

    username_already_exists = _user_exists(username)

    if username_already_exists:
        return render(request, 'profile.html', {
            'errors': {
                'username': 'Já está em uso.'
            }

        })

    current_user = User.objects.get(id=request.user.id)
    current_user.username = username.lower()
    current_user.save()

    return redirect('/auth/profile')


def update_user_password(request):
    if not request.user.is_authenticated:
        return render(request, "login.html")

    current_password = request.POST.get('currentPassword')
    new_password = str(request.POST.get('newPassword'))
    confirm_password = str(request.POST.get('confirmPassword'))

    if len(new_password.strip()) < 5:
        return render(request, "profile.html", {
            "errors": {
                "newPassword": "Senha muito curta."
            }
        })

    print('passwords', new_password, confirm_password)

    if new_password != confirm_password:
        return render(request, "profile.html", {
            "errors": {
                "confirmPassword": "Senhas não coincidem."
            }
        })

    user = User.objects.get(username=request.user.username)

    if not user.check_password(current_password):
        return render(request, "profile.html", {
            "errors": {
                "currentPassword": "Senha incorreta."
            }
        })

    print("new password", new_password)

    user.set_password(new_password)

    print("Hash pwd", user.password)

    user.save()

    # Manter o usuário autenticado após a mudança de senha
    update_session_auth_hash(request, user)

    return redirect('/auth/profile')


def _user_exists(username):
    return User.objects.filter(username=username).exists()


def _create_new_user(form):
    username = form.cleaned_data['username']
    email = form.cleaned_data['email']
    password = form.cleaned_data['password']

    user = User.objects.create_user(
        username=username.lower(), email=email, password=password
    )
    user.save()
