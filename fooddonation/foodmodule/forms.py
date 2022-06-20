from django import forms
from django.forms import ModelForm

from .models import *

class DonorForm(ModelForm):
    class Meta:
        model = Donor
        fields = ['name', 'email', 'password', 'phone']

class FoodDetailForm(ModelForm):
    class Meta:
        model = FoodDetail
        fields = '__all__'
        