from rest_framework import serializers
from .models import OrderItemModel


class OrderUserSerializer(serializers.ModelSerializer):
    size = serializers.SlugRelatedField(slug_field='size', read_only=True)
    color = serializers.SlugRelatedField(slug_field='color', read_only=True)
    product = serializers.SlugRelatedField(slug_field='product', read_only=True)
    class Meta:
        model = OrderItemModel
        fields = ['product', 'price', 'size', 'color', 'quantity', 'trace', 'created']
