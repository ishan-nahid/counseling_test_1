from django import forms 
from .models import User

class User_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'depertment', 'user_id', 'email', 'password', 'role']


class LoginForm(forms.Form):
    email = forms.EmailField(label='email')
    password = forms.CharField(label='password')
