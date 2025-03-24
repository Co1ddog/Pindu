# Create your views here.
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from people.models import User, UserAddress, Admin
from people.serializer import UserAddressSerializer, UserLoginSerializer, UserDetailSerializer, UserListSerializer, \
    AdminSerializer, AdminLoginSerializer


class UserRegister(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        nickname = request.data.get('nickname')
        password = request.data.get('password')
        if User.objects.filter(username=username).exists():
            resp = {
                'status': False,
                'data': '用户名已被注册'
            }
        else:
            user = User.objects.create_user(username=username, password=password, first_name=nickname)
            token, created = Token.objects.get_or_create(user=user)
            resp = {
                'status': True,
                'token': token.key,
                'user_id': user.pk,
                'user_name': user.username,
                'nickname': user.first_name,
            }
        return Response(resp)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserChangePw(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        new_pw = request.data.get('new_pw')

        user = User.objects.get(id=user_id)
        print(user.password)
        user.password = make_password(new_pw)
        print(user.password)
        user.save()
        return Response(self.get_serializer(user).data)


class UserList(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserListSerializer


class UserLogin(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)  # 生成Token
        return Response({
            'token': token.key,
            'user_id': user.pk,
        })


class UserPwVerify(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        pw = request.data.get('user_password')
        user = User.objects.get(id=user_id)

        flag = check_password(pw, user.password)
        print(flag)

        return Response({'status':flag})


class UserAddressListCreate(generics.ListCreateAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        receiver_name = request.data.get('receiver_name')
        receiver_phone = request.data.get('receiver_phone')
        receiver_region = request.data.get('receiver_region')
        receiver_place = request.data.get('receiver_place')

        if User.objects.filter(id=user_id).exists():
            useraddress = UserAddress.objects.create(user_id=user_id,
                                                     receiver_name=receiver_name,
                                                     receiver_phone=receiver_phone,
                                                     receiver_region=receiver_region,
                                                     receiver_place=receiver_place)
            useraddress.save()
            resp = {
                'status': True,
                'data': '已添加'
            }
        else:
            resp = {
                'status': False,
                'data': '用户不存在'
            }
        return Response(resp, status=200)


class UserAddressRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer

    def get(self, request, *args, **kwargs):
        uid = self.kwargs['pk']
        user = User.objects.get(id=uid)
        useraddress = self.get_queryset().filter(user=user)
        return Response(self.get_serializer(useraddress, many=True).data)


class AdminListCreate(generics.ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class AdminLogin(generics.ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminLoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        if Admin.objects.filter(username=username, pwd=password).exists():
            admin = Admin.objects.get(username=username, pwd=password)
            resp = {'status': True,
                    'admin_id': admin.id,
                    'name': admin.name,
                    'level': admin.level}
        else:
            resp = {'status': False}
        return Response(resp)
