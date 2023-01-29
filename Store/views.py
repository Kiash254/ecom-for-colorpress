from django.shortcuts import render
from .models import *
# Create your views here.



def Store(request):
    products = Product.objects.all()
    context = {
        'products':products
        
    }
    return render(request,'store.html',context)


def Cart(request):
    context = {}
    return render(request,'cart.html')

def Checkout(request):
    context = {}
    return render(request,'checkout.html')
