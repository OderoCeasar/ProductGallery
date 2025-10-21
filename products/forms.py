from django import forms
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=255, required=True, widget=forms.Textarea)
    price = forms.FloatField(required=True)
    image = forms.FileField(required=False)
