from django.db import models


# Create your models here.
class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, db_column='book_isbn')
    condition_rate = models.ForeignKey('ConditionRate', on_delete=models.CASCADE, related_name="+")
    book_num = models.IntegerField(default=0)


class Book(models.Model):
    isbn = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    writer = models.CharField(max_length=200, blank=True)
    intro = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=20, blank=True)
    presshouse = models.CharField(max_length=50, blank=True)
    pressdate = models.CharField(max_length=20, blank=True)
    price = models.FloatField(default=0, blank=True)
    picture = models.CharField(max_length=300, blank=True)
    isflow = models.BooleanField(default=True)


class ConditionRate(models.Model):
    id = models.AutoField(primary_key=True)
    condition = models.CharField(max_length=10)
    buy_rate = models.FloatField(default=1)
    sell_rate = models.FloatField(default=1)
