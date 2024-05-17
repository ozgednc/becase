from django import forms
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import validate_email, URLValidator
from django.core.exceptions import ValidationError
from .models import User, Ecommerce
import re

def validate_phone_num(val):
    phone_regexp = r'^\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$'
    if not re.fullmatch(phone_regexp, val):
        raise ValidationError("Phone number is invalid")
    return val


class UserInfo(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    user_email  = forms.EmailField(max_length=70, validators=[validate_email])
    phone = PhoneNumberField(null=False, validators=[validate_phone_num])
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'user_email', 'phone']

class CompanyInfo(forms.ModelForm):
    store_url = forms.URLField(max_length = 200, validators=[URLValidator()]) 
    PLATFORM_CHOICES = (
        ('Trendyol', 'Trendyol'),
        ('Hepsiburada', 'Hepsiburada'),
        ('Amazon', 'Amazon'),
    )
    platform = forms.ChoiceField(choices=PLATFORM_CHOICES)
    class Meta:
        model = Ecommerce
        fields = ['store_url', 'platform']