from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def CustomerList(request):
    return render(request,'customers.html')

def CustomerAdd(request):
    return render(request,'customers_add.html')

def CustomerDelete(request,id):
    selected_customer=Customer.objects.get(id=id)
    selected_customer.delete()

def CustomerUpdate(request,id):
    selected_customer=Customer.objects.get(id=id)
