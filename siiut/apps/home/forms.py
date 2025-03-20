from django import forms
from django.contrib.auth.forms import AuthenticationForm

input_tail = 'border border-gray-300 p-2 rounded-md shadow-sm focus:shadow-lg focus:ring focus:ring-blue-300 mt-4 mb-4 w-full'

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': input_tail, 
        'placeholder': 'Usuario'
        }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': input_tail, 
        'placeholder': 'Contraseña'
        }))