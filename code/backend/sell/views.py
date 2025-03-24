from rest_framework import generics
from rest_framework.response import Response

from book.models import Book, ConditionRate
from people.models import User, UserAddress
from sell.models import WareHouse, Order, OrderDetail
from sell.serializer import WarehouseSerializer, WarehouseCreateSerializer, SellOrderSerializer, \
    SellOrderDetailSerializer, SellOrderDetailPatchSerializer


class WarehouseListCreate(generics.ListCreateAPIView):
    queryset = WareHouse.objects.all()
    serializer_class = WarehouseCreateSerializer

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        book_isbn = request.data.get('isbn')
        customer_condition = request.data.get('customer_condition')

        warehouse = WareHouse.objects.create(user=User.objects.get(id=user_id),
                                             book=Book.objects.get(isbn=book_isbn),
                                             customer_condition=ConditionRate.objects.get(condition=customer_condition))
        warehouse.save()
        resp = {
            'status': True,
            'data': '已添加'
        }
        return Response(resp)


class WarehouseRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = WareHouse.objects.all()
    serializer_class = WarehouseSerializer


class WarehouseOfUserRetrieve(generics.RetrieveAPIView):
    queryset = WareHouse.objects.all()
    serializer_class = WarehouseSerializer

    def get(self, request, *args, **kwargs):
        uid = self.kwargs['pk']
        queryset = self.get_queryset().filter(user=User.objects.get(id=uid))
        # queryset = queryset.filter(user=User.objects.get(id=uid))
        serializer = WarehouseSerializer(queryset, many=True)
        return Response(serializer.data)


class SellOrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = SellOrderSerializer

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        useraddress_id = request.data.get('useraddress_id')

        user = User.objects.get(id=user_id)
        useraddress = UserAddress.objects.get(id=useraddress_id)
        order = Order.objects.create(user=user, useraddress=useraddress)
        order.save()
        return Response(self.get_serializer(order).data)


class SellOrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = SellOrderSerializer

    def get(self, request, *args, **kwargs):
        user_id = kwargs['pk']
        user = User.objects.get(id=user_id)
        order = Order.objects.filter(user=user)
        return Response(self.get_serializer(order, many=True).data)


class SellOrderDetailListCreate(generics.ListCreateAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = SellOrderDetailSerializer

    def post(self, request, *args, **kwargs):
        order_id = request.data.get('order_id')
        book_isbn = request.data.get('book_isbn')
        customer_condition = request.data.get('customer_condition')
        predict_price = request.data.get('predict_price')
        print(order_id, book_isbn, customer_condition, predict_price)
        order = Order.objects.get(id=order_id)
        book = Book.objects.get(isbn=book_isbn)
        c_condition = ConditionRate.objects.get(condition=customer_condition)
        orderdetial = OrderDetail.objects.create(order=order,
                                                 book=book,
                                                 customer_condition=c_condition,
                                                 predict_price=predict_price)
        orderdetial.save()
        return Response(self.get_serializer(orderdetial).data)


class SellOrderDetailRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = SellOrderDetailSerializer

    def get(self, request, *args, **kwargs):
        order_id = kwargs['pk']
        order = Order.objects.get(id=order_id)
        orderdetail = OrderDetail.objects.filter(order=order)
        return Response(self.get_serializer(orderdetail, many=True).data)


class SellOrderStatusList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = SellOrderSerializer

    def get(self, request, *args, **kwargs):
        status = kwargs['pk']
        return Response(self.get_serializer(self.get_queryset().filter(status=status), many=True).data)


class SellOrderDetailPatch(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = SellOrderDetailPatchSerializer
