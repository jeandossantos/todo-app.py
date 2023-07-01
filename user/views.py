from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password as encrypt_password

from .models import User
from .forms import RegisterUserForm

def create_user(request):
    if request.method == 'GET': return render(request, 'register.html')
    
    if request.method == 'POST':        
        form = RegisterUserForm(request.POST)
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
            return render(request, 'register.html', {'form': form  })
            

def login(request):
    if request.method == 'GET': return render(request, 'login.html')    
    
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