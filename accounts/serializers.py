from rest_framework import serializers
from .models import User, AddressModel


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'birthdate', 'password']


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=200)


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressModel
        fields = ['id', 'first_name_address', 'last_name_address', 'company', 'VAT_number', 'address',
                  'address_complement', 'phone_number', 'postal_code', 'city', 'country', 'identification_number']


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'birthdate', 'password']
