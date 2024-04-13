from rest_framework import serializers
from .models import OrderItemModel


class OrderUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItemModel
        fields = ['product', 'price', 'size', 'color', 'quantity', 'trace', 'created']
