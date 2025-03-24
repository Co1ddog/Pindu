from django.db import models


# Create your models here.
class WareHouse(models.Model):
    user = models.ForeignKey('people.User', related_name='+', on_delete=models.CASCADE)
    book = models.ForeignKey('book.Book', on_delete=models.CASCADE, db_column='book_isbn')

    id = models.AutoField(primary_key=True)
    customer_condition = models.ForeignKey('book.ConditionRate', on_delete=models.CASCADE, related_name="+")


class Order(models.Model):
    user = models.ForeignKey('people.User', related_name='+', on_delete=models.CASCADE)
    useraddress = models.ForeignKey('people.UserAddress', related_name="sell", on_delete=models.CASCADE)

    id = models.AutoField(primary_key=True)
    status = models.IntegerField(default=0)
    submit_time = models.DateTimeField(auto_now_add=True)
    finish_time = models.DateTimeField(null=True)


class OrderDetail(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    book = models.ForeignKey('book.Book', on_delete=models.CASCADE, db_column='book_isbn')

    id = models.AutoField(primary_key=True)
    customer_condition = models.ForeignKey('book.ConditionRate', on_delete=models.CASCADE, related_name="+")
    final_condition = models.ForeignKey('book.ConditionRate', on_delete=models.CASCADE, related_name="+", null=True)
    predict_price = models.FloatField(null=True)
    final_price = models.FloatField(null=True)
