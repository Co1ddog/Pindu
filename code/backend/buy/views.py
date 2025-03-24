from rest_framework import generics
from rest_framework.response import Response

from book.models import Book, Inventory, ConditionRate
from buy.models import Cart, Order, OrderDetail
from buy.serializer import CartSerializer, BuyOrderSerializer, BuyOrderDetailSerializer, CartRetrieveSerializer
from people.models import User, UserAddress


# Create your views here.
class CartListCreate(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        book_isbn = request.data.get('inventory_book_isbn')
        conditionrate_name = request.data.get('inventory_conditionrate_name')
        book_num = request.data.get('book_num')

        user = User.objects.get(id=user_id)
        book = Book.objects.get(isbn=book_isbn)
        conditionrate = ConditionRate.objects.get(condition=conditionrate_name)
        inventory = Inventory.objects.filter(book=book, condition_rate=conditionrate).first()

        print(Cart.objects.filter(user=user, inventory=inventory).exists())

        if Cart.objects.filter(user=user, inventory=inventory).exists():
            cart = Cart.objects.get(user=user, inventory=inventory)
            cart.book_num += 1
            cart.save()
        else:
            cart = Cart.objects.create(user=user, inventory=inventory, book_num=book_num)
            cart.save()
        return Response(self.get_serializer(cart).data)


class CartMinus(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        inventory_id = request.data.get('inventory')

        user = User.objects.get(id=user_id)
        inventory = Inventory.objects.get(id=inventory_id)
        cart = Cart.objects.get(user=user, inventory=inventory)
        cart.book_num -= 1
        cart.save()
        return Response(self.get_serializer(cart).data)


class CartRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get(self, request, *args, **kwargs):
        user_id = kwargs['pk']
        user = User.objects.get(id=user_id)

        # !!todo!!使用 values() 方法选择了 age 字段来进行分组。然后，我们使用 annotate() 方法添加了一个名为 total 的新属性，该属性以 Customer 模型的 id 字段进行计数。
        cart = Cart.objects.filter(user=user)
        return Response(CartRetrieveSerializer(cart, many=True).data)
        # return Response(self.get_serializer(cart, many=True).data)


class CartInventoryNumRetrieve(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get(self, request, *args, **kwargs):
        user_id = kwargs['pk']
        isbn = kwargs['qk']
        condition_name = kwargs['ok']
        print(request)
        user = User.objects.get(id=user_id)
        book = Book.objects.get(isbn=isbn)
        cr = ConditionRate.objects.get(condition=condition_name)
        inv = Inventory.objects.get(book=book, condition_rate=cr)
        q = Cart.objects.get(user=user, inventory=inv)
        return Response(self.get_serializer(q).data)


class BuyOrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = BuyOrderSerializer

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        useraddress_id = request.data.get('useraddress_id')

        user = User.objects.get(id=user_id)
        useraddress = UserAddress.objects.get(id=useraddress_id)
        order = Order.objects.create(user=user, useraddress=useraddress)
        order.save()
        return Response(self.get_serializer(order).data)


class BuyOrderRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = BuyOrderSerializer

    def get(self, request, *args, **kwargs):
        user_id = kwargs['pk']
        user = User.objects.get(id=user_id)
        order = Order.objects.filter(user=user)
        return Response(self.get_serializer(order, many=True).data)


class BuyOrderDetailListCreate(generics.ListCreateAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = BuyOrderDetailSerializer

    def post(self, request, *args, **kwargs):
        order_id = request.data.get('order_id')
        inventory_book_isbn = request.data.get('inventory_book_isbn')
        inventory_conditionrate_condition = request.data.get('inventory_conditionrate_condition')
        book_num = request.data.get('book_num')
        order_book_price = request.data.get('order_book_price')

        order = Order.objects.get(id=order_id)
        book = Book.objects.get(isbn=inventory_book_isbn)
        conditionrate = ConditionRate.objects.get(condition=inventory_conditionrate_condition)
        inventory = Inventory.objects.get(book=book, condition_rate=conditionrate)
        orderdetail = OrderDetail.objects.create(order=order, inventory=inventory, book_num=book_num,
                                                 order_book_price=order_book_price)
        orderdetail.save()
        return Response(self.get_serializer(orderdetail).data)


class BuyOrderDetailRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = BuyOrderDetailSerializer

    def get(self, request, *args, **kwargs):
        order_id = kwargs['pk']
        order = Order.objects.get(id=order_id)
        orderdetail = OrderDetail.objects.filter(order=order)
        return Response(self.get_serializer(orderdetail, many=True).data)
