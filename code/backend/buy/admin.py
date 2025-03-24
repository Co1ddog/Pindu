from django.contrib import admin

from buy.models import Cart, OrderDetail, Order

# Register your models here.
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderDetail)
