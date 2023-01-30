from django.shortcuts import render,redirect
from .models import *
# Create your views here.



def Store(request):
    products = Product.objects.all()
    context = {
        'products':products
        
    }
    return render(request,'store.html',context)


def Cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
    context = {
            'items':items,
            'order':order,
        }
    return render(request,'cart.html',context)


def Checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
    context = {
            'items':items,
            'order':order,
        }
    return render(request,'checkout.html',context)


def UpdateItem(request,pk):
    product = Product.objects.get(id=pk)
    order,created = Order.objects.get_or_create(customer=request.user.customer,complete=False)
    orderItem,created = OrderItem.objects.get_or_create(order=order,product=product)
    orderItem.save()
    return redirect('store')
    
    