from rest_framework import serializers

from sell.models import WareHouse, Order, OrderDetail


class WarehouseSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id')
    book_name = serializers.CharField(source='book.name')
    book_isbn = serializers.CharField(source='book.isbn')
    book_pic = serializers.CharField(source='book.picture')
    book_price = serializers.FloatField(source='book.price')
    book_writer = serializers.CharField(source='book.writer')
    condition_rate_name = serializers.CharField(source='customer_condition.condition')
    condition_rate_customerrate = serializers.FloatField(source='customer_condition.sell_rate')

    class Meta:
        model = WareHouse
        # fields = ['id', 'user_id', 'book_name', 'book_isbn', 'book_pic', 'customer_condition', 'sell_price']
        fields = ['id', 'user_id', 'book_name', 'book_isbn', 'book_pic', 'book_price', 'book_writer',
                  'condition_rate_name',
                  'condition_rate_customerrate']


class WarehouseCreateSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id')
    book_isbn = serializers.CharField(source='book.isbn')

    class Meta:
        model = WareHouse
        fields = ['id', 'user_id', 'book_isbn', 'customer_condition']


class SellOrderSerializer(serializers.ModelSerializer):
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


class SellOrderDetailSerializer(serializers.ModelSerializer):
    customer_condition = serializers.CharField(source='customer_condition.condition')
    customer_conditionrate = serializers.CharField(source='customer_condition.sell_rate')
    final_condition = serializers.CharField(source='final_condition.condition', allow_null=True)
    final_conditionrate = serializers.CharField(source='final_condition.buy_rate', allow_null=True)
    order_id = serializers.IntegerField(source='order.id')
    book_isbn = serializers.CharField(source='book.isbn')
    book_name = serializers.CharField(source='book.name')
    book_writer = serializers.CharField(source='book.writer')
    book_picture = serializers.CharField(source='book.picture')
    book_price = serializers.FloatField(source='book.price')

    class Meta:
        model = OrderDetail
        fields = ['id', 'order_id', 'book_isbn', 'book_name', 'book_writer', 'book_picture', 'book_price',
                  'customer_condition', 'customer_conditionrate',
                  'final_condition', 'final_conditionrate',
                  'predict_price', 'final_price']


class SellOrderDetailPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = "__all__"
