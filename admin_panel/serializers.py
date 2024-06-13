from rest_framework.serializers import Serializer, ModelSerializer
from product.models import ProductModel, ProductCategoryModel


class ProductSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategoryModel
        fields = '__all__'
