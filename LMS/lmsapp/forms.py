from lmsapp.models import Login
from lmsapp.models import Register
from django import forms


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = "__all__"
        
        widgets = {
            'user_name': forms.TextInput(attrs={'placeholder': 'user_name'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'password'}),
        }
       

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = "__all__"
        
        widgets = {
            'user_name': forms.TextInput(attrs={'placeholder': 'user_name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'password'}),
            'confirm_password': forms.PasswordInput(attrs={'placeholder': 'confirm_password'}),
        }
