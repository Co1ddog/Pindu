from rest_framework import serializers

from .models import User, Admin, UserAddress


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name']


class AdminLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'username', 'pwd', 'level']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserAddressSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id')

    class Meta:
        model = UserAddress
        fields = ['id', 'user_id', 'receiver_name', 'receiver_phone', 'receiver_region', 'receiver_place']


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

