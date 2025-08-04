from django.shortcuts import render,redirect
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

    context={
        'customer_form':Customer_Form(instance=selected_customer)
    }

    if request.method=='POST':
        customer_form=Customer_Form(request.POST,instance=selected_customer)

        if customer_form.is_valid():
            customer_form.save()
            return redirect('/Update/customer/')

    return render(request,'customers_add.html',context)