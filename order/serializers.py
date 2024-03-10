from rest_framework import serializers
from .models import OrderItemModel


class OrderUserSerializer(serializers.Serializer):
    class Meta:
        model = OrderItemModel
        fields = ['product', 'price', 'color', 'size', 'quantity']


