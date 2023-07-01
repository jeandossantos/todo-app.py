from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=5)


class LoginForm(forms.Form):
    username = forms.CharField(min_length=2, max_length=65)
    password = forms.CharField(widget=forms.PasswordInput, min_length=5)
