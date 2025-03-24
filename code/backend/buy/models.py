from django.db import models


# Create your models here.
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('people.User', related_name='+', on_delete=models.CASCADE)
    inventory = models.ForeignKey('book.Inventory', on_delete=models.CASCADE)  # 一本某个品相的书

    book_num = models.IntegerField(default=1)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('people.User', related_name='+', on_delete=models.CASCADE)
    useraddress = models.ForeignKey('people.UserAddress', related_name="buy", on_delete=models.CASCADE)

    status = models.IntegerField(default=0)
    submit_time = models.DateTimeField(auto_now_add=True)
    finish_time = models.DateTimeField(null=True)


class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    inventory = models.ForeignKey('book.Inventory', on_delete=models.CASCADE)

    book_num = models.IntegerField(default=1)
    order_book_price = models.FloatField(default=0.0)
