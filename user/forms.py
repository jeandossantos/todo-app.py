from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=65)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=5)
    
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=5)