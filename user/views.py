from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#from .models import User

def create_user(request):
    
    return render(request, 'register.html')

    