from rest_framework import serializers

from buy.models import Cart, Order, OrderDetail


class CartSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id')
    user_name = serializers.CharField(source='user.username')
    inventory_book_isbn = serializers.CharField(source='inventory.book.isbn')
    inventory_book_name = serializers.CharField(source='inventory.book.name')
    inventory_conditionrate_name = serializers.CharField(source='inventory.condition_rate.condition')
    inventory_conditionrate_buyrate = serializers.FloatField(source='inventory.condition_rate.buy_rate')
    inventory_book_writer = serializers.CharField(source='inventory.book.writer')
    inventory_book_price = serializers.CharField(source='inventory.book.price')
    inventory_book_picture = serializers.CharField(source='inventory.book.picture')

    class Meta:
        model = Cart
        fields = ['id', 'user_id', 'user_name',
                  'inventory_book_isbn', 'inventory_book_name', 'inventory_book_writer', 'inventory_book_price',
                  'inventory_book_picture',
                  'inventory_conditionrate_name', 'inventory_conditionrate_buyrate',
                  'book_num']


class CartRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class BuyOrderSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id')
    user_name = serializers.CharField(source='user.first_name')
    useraddress_id = serializers.IntegerField(source='useraddress.id')
    useraddress_receiver_name = serializers.CharField(source='useraddress.receiver_name')
    useraddress_receiver_phone = serializers.CharField(source='useraddress.receiver_phone')
    useraddress_receiver_region = serializers.CharField(source='useraddress.receiver_region')
    useraddress_receiver_place = serializers.CharField(source='useraddress.receiver_place')


    class Meta:
        model = Order
        fields = ['id', 'user_id', 'user_name',
                  'useraddress_id', 'useraddress_receiver_name', 'useraddress_receiver_phone',
                  'useraddress_receiver_region', 'useraddress_receiver_place',
                  'status', 'submit_time', 'finish_time']


# 创建buyorderdetail记录时的序列化器
class BuyOrderDetailSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField(source='order.id')
    inventory_book_isbn = serializers.CharField(source='inventory.book.isbn')
    inventory_book_name = serializers.CharField(source='inventory.book.name')
    inventory_book_writer = serializers.CharField(source='inventory.book.writer')
    inventory_book_picture = serializers.CharField(source='inventory.book.picture')
    inventory_conditionrate_condition = serializers.CharField(source='inventory.condition_rate.condition')

    # 序列化器里的字段，在post里可以不存在
    inventory_id = serializers.IntegerField(source='inventory.id')

    class Meta:
        model = OrderDetail
        fields = ['id', 'order_id', 'inventory_id', 'inventory_book_isbn', 'inventory_book_name',
                  'inventory_book_writer', 'inventory_book_picture', 'inventory_conditionrate_condition',
                  'book_num', 'order_book_price']
