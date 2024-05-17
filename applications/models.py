from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_email  = models.EmailField(max_length=70,blank=True,unique=True)
    phone = PhoneNumberField(blank=False, unique=True)

class Ecommerce(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="owners")
    store_url = models.URLField(max_length = 200) 
    platform = models.CharField(max_length=11)
    
