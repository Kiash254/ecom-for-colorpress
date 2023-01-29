from django.contrib import admin
from .models import  Customer, Product, Order, OrderItem, ShippingAddress
# Register your models here.


admin.site.site_header = 'Admin Dashboard'
admin.site.site_title = 'Admin Dashboard'
admin.site.index_title = 'Welcome to Admin Dashboard'

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
    
