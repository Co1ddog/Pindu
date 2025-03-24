from django.contrib import admin

from sell.models import Order, WareHouse, OrderDetail

admin.site.register(WareHouse)
admin.site.register(Order)
admin.site.register(OrderDetail)
