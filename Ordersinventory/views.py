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
            return redirect('/orders/all/customers/')

    return render(request,'customers_add.html',context)

def OrdersAdd(request):

    context={
        'order_form':Orders_Form()
    }

    if request.method=="POST":
        selected_product=Product.objects.get(id=request.POST['product_reference'])
        amount=float(selected_product.price)*float(request.POST['quantity'])
        gst_amount=(amount*selected_product.gst)/100
        bill_amount=amount+gst_amount

        new_order=Orders(customer_reference_id=request.POST['customer_reference'],
                         product_reference_id=request.POST['product_reference'],
                         order_number=request.POST['order_number'],
                         order_date=request.POST['order_date'],
                         quantity=request.POST['quantity'],
                         amount=request.POST['amount'],
                         gst_amount=gst_amount,
                         bill_amount=bill_amount)
        
        new_order.save()

    return render(request,'orders_add.html',context)

def OrdersList(request):

    context={
        'all_orders':Orders.objects.all()
    }

    return render(request,'orders.html',context)