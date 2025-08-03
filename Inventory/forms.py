from django.forms import ModelForm
from .models import *

class Product_Form(ModelForm):
    class Meta:
        model=Product
        fields='__all__'

class Product_Form1(ModelForm):
    class Meta:
        model=Product
        fields=[]