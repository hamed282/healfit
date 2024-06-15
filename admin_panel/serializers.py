from rest_framework.serializers import Serializer, ModelSerializer
from product.models import ProductModel, ProductCategoryModel
from accounts.models import User


class ProductSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategoryModel
        fields = '__all__'


class LoginUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']
