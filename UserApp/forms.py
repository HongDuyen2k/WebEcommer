from cProfile import label
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import TextInput, EmailInput, Select, FileInput
from models.models import (
    UserProfile
)


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length = 100, 
        label = 'Tài khoản', 
        widget = forms.TextInput(attrs = {'placeholder': 'demo123'})
    )
    email = forms.EmailField(
        max_length = 200, 
        label = 'Email', 
        widget = forms.EmailInput(attrs = {'placeholder': 'demo@gmail.com'})
    )
    first_name = forms.CharField(
        max_length = 100, 
        label = 'Họ', 
        widget = forms.TextInput(attrs = {'placeholder': 'Nguyễn Văn'})
    )
    last_name = forms.CharField(
        max_length = 100, 
        label = 'Tên', 
        widget = forms.TextInput(attrs = {'placeholder': 'ABC'})
    )
    password1 = forms.CharField(
        max_length = 100, 
        label = 'Mật khẩu', 
        widget = forms.PasswordInput(attrs = {'placeholder': '************', 'class': 'form-control'})
    )
    password2 = forms.CharField(
        max_length = 100, 
        label = 'Xác nhận lại mật khẩu', 
        widget = forms.PasswordInput(attrs = {'placeholder': '************', 'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']






   
   
  
  

   
       
    