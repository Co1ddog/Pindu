from rest_framework import serializers

from book.models import Book, ConditionRate, Inventory


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class ConditionRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConditionRate
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'


class InventoryDetailSerializer(serializers.ModelSerializer):
    book_isbn = serializers.IntegerField(source='book.isbn')
    book_name = serializers.CharField(source='book.name')
    book_pic = serializers.CharField(source='book.picture')
    book_price = serializers.FloatField(source='book.price')
    book_writer = serializers.CharField(source='book.writer')
    condition_rate_customerrate = serializers.FloatField(source='condition_rate.buy_rate')
    condition_rate_name = serializers.CharField(source='condition_rate.condition')

    class Meta:
        model = Inventory
        fields = ['id', 'condition_rate', 'book_isbn', 'book_name', 'book_pic', 'book_price', 'book_writer',
                  'condition_rate_customerrate', 'condition_rate_name', 'book_num']
