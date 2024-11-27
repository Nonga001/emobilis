from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('auth/register/',views.register,name='register'),
    path('auth/login/',views.login,name='login'),
]