from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.

def ProductsAdd(request):
    context={
        'product_form':Product_Form()
    }
    if request.method == 'POST':
        # print(request.POST)
        product_form=Product_Form(request.POST)

        if product_form.is_valid():
            product_form.save()

    return render(request,'products_add.html',context)

def AllProducts(request):
    
    context={
        'all_products':Product.objects.all()
    }

    return render(request,'products.html',context)

def DeleteProducts(request,id):
    selected_product=Product.objects.get(id=id)
    selected_product.delete()

    return redirect('/inventory/products/')

def ProductUpdate(request,id):
    selected_product=Product.objects.get(id=id)

    context={
        'product_form':Product_Form(instance=selected_product)
    }

    if request.method=='POST':
        product_form=Product_Form(request.POST,instance=selected_product)

        if product_form.is_valid():
            product_form.save()
            return redirect('/inventory/products/')

    return render(request,'products_add.html',context)