from django.contrib import admin

from people.models import Admin, User, UserAddress

# Register your models here.
admin.site.register(Admin)
admin.site.register(User)
admin.site.register(UserAddress)
