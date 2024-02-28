from rest_framework import serializers
from .models import ProductCategoryModel, PopularProductModel, ProductModel, ProductVariantModel, ColorProductModel,\
    SizeProductModel


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategoryModel
        fields = '__all__'


class PopularProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularProductModel
        fields = ['popular']
        depth = 1


class ProductVariantSerializer(serializers.ModelSerializer):
    size = serializers.SlugRelatedField(read_only=True, slug_field='size')
    color = serializers.SlugRelatedField(read_only=True, slug_field='color')

    class Meta:
        model = ProductVariantModel
        fields = ['quantity', 'color', 'size']


class ProductSerializer(serializers.ModelSerializer):
    product_color_size = ProductVariantSerializer(many=True, read_only=True)
    off_price = serializers.SerializerMethodField()

    class Meta:
        model = ProductModel
        fields = ['product', 'image1', 'image2', 'image3', 'image4', 'image5', 'price', 'off_price', 'percent_discount',
                  'product_code', 'slug', 'created', 'updated', 'product_color_size', 'id']

    def get_off_price(self, obj):
        price = obj.price
        percent_discount = obj.percent_discount
        if obj.percent_discount is None:
            percent_discount = 0
        return int(price - price * percent_discount / 100)


class ProductCartSerializer(serializers.ModelSerializer):
    product_color_size = ProductVariantSerializer(many=True, read_only=True)
    off_price = serializers.SerializerMethodField()

    class Meta:
        model = ProductModel
        fields = ['id', 'product', 'image1', 'price', 'off_price', 'slug', 'product_color_size']

    def get_off_price(self, obj):
        price = obj.price
        percent_discount = obj.percent_discount
        if obj.percent_discount is None:
            percent_discount = 0
        return int(price - price * percent_discount / 100)


class QuantityProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductVariantModel
        fields = ['quantity']


class ProductListSerializer(serializers.ModelSerializer):
    off_price = serializers.SerializerMethodField()

    class Meta:
        model = ProductModel
        fields = ['category', 'product', 'image1', 'price', 'off_price', 'percent_discount',
                  'product_code', 'slug']

    def get_off_price(self, obj):
        price = obj.price
        percent_discount = obj.percent_discount
        if obj.percent_discount is None:
            percent_discount = 0
        return int(price - price * percent_discount / 100)
