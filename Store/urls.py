#import urls and views
from django.urls import path

from .views import Store, Cart, Checkout


app_name='Store'

urlpatterns=[
    path('',Store,name='Store'),
    path('Cart/',Cart,name='Cart'),
    path('Checkout/',Checkout,name='Checkout'),
]