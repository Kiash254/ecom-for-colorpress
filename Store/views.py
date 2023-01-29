from django.shortcuts import render

# Create your views here.



def Store(request):
    context = {}
    return render(request,'store.html',context)


def Cart(request):
    context = {}
    return render(request,'cart.html')

def Checkout(request):
    context = {}
    return render(request,'Checkout.html')
