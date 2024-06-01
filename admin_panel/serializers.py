from rest_framework.serializers import Serializer, ModelSerializer
from product.models import ProductModel


class ProductSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'
