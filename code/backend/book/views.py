from django.db.models import Count, Sum, QuerySet
from rest_framework import generics
from rest_framework.response import Response

from book.models import Book, ConditionRate, Inventory
from book.serializer import BookSerializer, ConditionRateSerializer, InventorySerializer, InventoryDetailSerializer


class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'isbn'

    def get(self, request, *args, **kwargs):
        isbn = self.kwargs['isbn']
        print(isbn)
        if Book.objects.filter(isbn=isbn).exists():
            book = Book.objects.get(isbn=isbn)
            resp = {
                'status': True,
                'isbn': book.isbn,
                'name': book.name,
                'writer': book.writer,
                'category': book.category,
                'presshouse': book.presshouse,
                'pressdate': book.pressdate,
                'price': book.price,
                'picture': book.picture,
                'isflow': book.isflow,
                'intro': book.intro,
            }
        else:
            resp = {
                'status': False,
                'data': '书不存在',
                'isbn': isbn,
            }
        return Response(resp, status=200)


class BookIsFlowList(generics.ListAPIView):
    queryset = Book.objects.filter(isflow=True)
    serializer_class = BookSerializer


class BookCategoryList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        book = self.get_queryset().values('category').annotate(total=Count('isbn'))
        resultset = []
        for i in book:
            resultset.append(i)
        return Response(resultset)


class BookRetrieveByCategory(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        category = kwargs['pk']
        # presshouse = kwargs['qk']
        print(category)
        # print(presshouse)
        book = self.get_queryset().filter(category=category)
        return Response(self.get_serializer(book, many=True).data)


class BookPressList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        book = self.get_queryset().values('presshouse').annotate(total=Count('isbn'))
        resultset = []
        for i in book:
            resultset.append(i)
        return Response(resultset)


class BookRetrieveByPresshouse(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        press = kwargs['pk']
        book = self.get_queryset().filter(presshouse=press)
        return Response(self.get_serializer(book, many=True).data)


# ---------------------------------------------------------------------------------------------------------
class BookRetrieveByCatePressPriceSearch(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        cate = kwargs['pk']
        press = kwargs['qk']
        price = kwargs['ok']
        search = kwargs['rk']
        haveinv = kwargs['sk']
        if price != '-':
            price = [int(i) for i in price.split(',')]
        if search == '-':
            search = ''
        print(search)

        queryset = QuerySet
        if haveinv == '只看有货':
            book_haveinv = Inventory.objects.all().values("book").annotate(total=Sum("book_num"))
            book_haveinv_isbn = [i['book'] for i in book_haveinv]
            print(book_haveinv_isbn)
            # 有库存的book queryset
            queryset = Book.objects.filter(isbn__in=book_haveinv_isbn)
        elif haveinv == '-':
            queryset = self.get_queryset()
        print(queryset)

        if cate != '-' and press != '-' and price != '-':
            book = queryset.filter(category=cate, presshouse=press, price__range=price,
                                   name__icontains=search)
        elif cate == '-' and press != '-' and price != '-':
            book = queryset.filter(presshouse=press, price__range=price, name__icontains=search)
        elif cate != '-' and press == '-' and price != '-':
            book = queryset.filter(category=cate, price__range=price, name__icontains=search)
        elif cate != '-' and press != '-' and price == '-':
            book = queryset.filter(category=cate, presshouse=press, name__icontains=search)
        elif cate != '-' and press == '-' and price == '-':
            book = queryset.filter(category=cate, name__icontains=search)
        elif cate == '-' and press != '-' and price == '-':
            book = queryset.filter(presshouse=press, name__icontains=search)
        elif cate == '-' and press == '-' and price != '-':
            book = queryset.filter(price__range=price, name__icontains=search)
        elif cate == '-' and press == '-' and price == '-':
            book = queryset.filter(name__icontains=search)
        return Response(self.get_serializer(book, many=True).data)


class BookCategoryListByCatePressPriceSearch(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        cate = kwargs['pk']
        press = kwargs['qk']
        price = kwargs['ok']
        search = kwargs['rk']
        haveinv = kwargs['sk']
        if price != '-':
            price = [int(i) for i in price.split(',')]
        if search == '-':
            search = ''

        queryset = QuerySet
        if haveinv == '只看有货':
            book_haveinv = Inventory.objects.all().values("book").annotate(total=Sum("book_num"))
            book_haveinv_isbn = [i['book'] for i in book_haveinv]
            print(book_haveinv_isbn)
            # 有库存的book queryset
            queryset = Book.objects.filter(isbn__in=book_haveinv_isbn)
        elif haveinv == '-':
            queryset = self.get_queryset()
        print(queryset)

        if cate != '-' and press != '-' and price != '-':
            book = queryset.filter(category=cate, presshouse=press, price__range=price,
                                   name__icontains=search).values(
                'category').annotate(total=Count('isbn'))
        elif cate == '-' and press != '-' and price != '-':
            book = queryset.filter(presshouse=press, price__range=price, name__icontains=search).values(
                'category').annotate(total=Count('isbn'))
        elif cate != '-' and press == '-' and price != '-':
            book = queryset.filter(category=cate, price__range=price, name__icontains=search).values(
                'category').annotate(total=Count('isbn'))
        elif cate != '-' and press != '-' and price == '-':
            book = queryset.filter(category=cate, presshouse=press, name__icontains=search).values(
                'category').annotate(total=Count('isbn'))
        elif cate != '-' and press == '-' and price == '-':
            book = queryset.filter(category=cate, name__icontains=search).values(
                'category').annotate(total=Count('isbn'))
        elif cate == '-' and press != '-' and price == '-':
            book = queryset.filter(presshouse=press, name__icontains=search).values(
                'category').annotate(total=Count('isbn'))
        elif cate == '-' and press == '-' and price != '-':
            book = queryset.filter(price__range=price, name__icontains=search).values(
                'category').annotate(total=Count('isbn'))
        elif cate == '-' and press == '-' and price == '-':
            book = queryset.filter(name__icontains=search).values(
                'category').annotate(total=Count('isbn'))
        resultset = []
        for i in book:
            resultset.append(i)
        return Response(resultset)


class BookPresshouseListByCatePressPriceSearch(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        cate = kwargs['pk']
        press = kwargs['qk']
        price = kwargs['ok']
        search = kwargs['rk']
        haveinv = kwargs['sk']
        if price != '-':
            price = [int(i) for i in price.split(',')]
        if search == '-':
            search = ''

        queryset = QuerySet
        if haveinv == '只看有货':
            book_haveinv = Inventory.objects.all().values("book").annotate(total=Sum("book_num"))
            book_haveinv_isbn = [i['book'] for i in book_haveinv]
            print(book_haveinv_isbn)
            # 有库存的book queryset
            queryset = Book.objects.filter(isbn__in=book_haveinv_isbn)
        elif haveinv == '-':
            queryset = self.get_queryset()
        print(queryset)

        if cate != '-' and press != '-' and price != '-':
            book = queryset.filter(category=cate, presshouse=press, price__range=price,
                                   name__icontains=search).values(
                'presshouse').annotate(total=Count('isbn'))
        elif cate == '-' and press != '-' and price != '-':
            book = queryset.filter(presshouse=press, price__range=price, name__icontains=search).values(
                'presshouse').annotate(total=Count('isbn'))
        elif cate != '-' and press == '-' and price != '-':
            book = queryset.filter(category=cate, price__range=price, name__icontains=search).values(
                'presshouse').annotate(total=Count('isbn'))
        elif cate != '-' and press != '-' and price == '-':
            book = queryset.filter(category=cate, presshouse=press, name__icontains=search).values(
                'presshouse').annotate(total=Count('isbn'))
        elif cate != '-' and press == '-' and price == '-':
            book = queryset.filter(category=cate, name__icontains=search).values(
                'presshouse').annotate(total=Count('isbn'))
        elif cate == '-' and press != '-' and price == '-':
            book = queryset.filter(presshouse=press, name__icontains=search).values(
                'presshouse').annotate(total=Count('isbn'))
        elif cate == '-' and press == '-' and price != '-':
            book = queryset.filter(price__range=price, name__icontains=search).values(
                'presshouse').annotate(total=Count('isbn'))
        elif cate == '-' and press == '-' and price == '-':
            book = queryset.filter(name__icontains=search).values(
                'presshouse').annotate(total=Count('isbn'))
        resultset = []
        for i in book:
            resultset.append(i)
        return Response(resultset)


# class BookSearchList(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     def get(self, request, *args, **kwargs):
#         book_name = kwargs['pk']
#         book = self.get_queryset().filter(name__icontains=book_name)
#         return Response(self.get_serializer(book, many=True).data)


class ConditionRateListCreate(generics.ListCreateAPIView):
    queryset = ConditionRate.objects.all()
    serializer_class = ConditionRateSerializer


class InventoryListCreate(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def post(self, request, *args, **kwargs):
        add_num = request.data.get('book_num')
        book_isbn = request.data.get('book')
        condition_rate_id = request.data.get('condition_rate')
        cr = ConditionRate.objects.get(id=condition_rate_id)
        book = Book.objects.get(isbn=book_isbn)
        if Inventory.objects.filter(book=book, condition_rate=cr).exists():
            inv = Inventory.objects.get(book=book, condition_rate=cr)
            inv.book_num += int(add_num)
            inv.save()
        else:
            inv = Inventory.objects.create(book=book, condition_rate=cr, book_num=1)
            inv.save()
        return Response(self.get_serializer(inv).data)


class InventoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def get(self, request, *args, **kwargs):
        isbn = self.kwargs['pk']
        if Book.objects.filter(isbn=isbn).exists():
            if Inventory.objects.filter(book=Book.objects.get(isbn=isbn)).exists():
                inventory = Inventory.objects.filter(book=Book.objects.get(isbn=isbn)).values(
                    'condition_rate').annotate(total=Sum('book_num'))
                rs = []
                for i in inventory:
                    rs.append(i)
                # return Response(self.get_serializer(inventory, many=True).data)
                return Response(rs)
            else:
                return Response([{'condition_rate': '此书无库存', 'total': 0, 'buy_rate': 0}])
        else:
            return Response([{'condition_rate': '此书不存在', 'total': 0, 'buy_rate': 0}])


class InventoryDetailRetrieve(generics.RetrieveAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryDetailSerializer

    def get(self, request, *args, **kwargs):
        inv_id = kwargs['pk']
        inventory = self.get_queryset().get(id=inv_id)
        return Response(self.get_serializer(inventory).data)


class ConditionRateRetreiveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConditionRate.objects.all()
    serializer_class = ConditionRateSerializer
