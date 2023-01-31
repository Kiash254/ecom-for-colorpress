#import urls and views
from django.urls import path

from .views import Store, Cart, Checkout,UpdateItem,ProcessOrder


app_name='store'

urlpatterns=[
    path('',Store,name='store'),
    path('cart/',Cart,name='cart'),
    path('checkout/',Checkout,name='checkout'),
    path('update_item/',UpdateItem,name='update_item'),
    path('process_order/',ProcessOrder,name='process_order')
]