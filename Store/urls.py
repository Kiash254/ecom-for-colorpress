#import urls and views
from django.urls import path

from .views import Store, Cart, Checkout


app_name='Store'

urlpatterns=[
    path('',Store,name='store'),
    path('cart/',Cart,name='cart'),
    path('checkout/',Checkout,name='checkout'),
]