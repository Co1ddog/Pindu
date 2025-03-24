from django.contrib import admin

from book.models import Book, Inventory, ConditionRate

# Register your models here.
admin.site.register(Book)
admin.site.register(Inventory)
admin.site.register(ConditionRate)
