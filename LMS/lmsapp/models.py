from django.db import models

# Create your models here.

class Login(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
   
    def __str__(self):
       return self.user_name
     
class Register(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    
    def __str__(self):
      return self.user_name