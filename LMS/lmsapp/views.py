from django.shortcuts import render
from lmsapp.forms import LoginForm, RegisterForm
from lmsapp.models import Login, Register

# Create your views here.
def home(request):
    return render(request, 'lmsapp/home.html')

def login(request):
    return render(request, 'lmsapp/auth/login.html', {'form': LoginForm()})
  
    

def register(request):
    return render(request, 'lmsapp/auth/register.html', {'form': RegisterForm()})