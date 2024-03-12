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


class SizeSerializer(serializers.ModelSerializer):
    size = serializers.SlugRelatedField(read_only=True, slug_field='size')

    class Meta:
        model = ProductVariantModel
        fields = ['size']

# class ProductSerializer(serializers.ModelSerializer):
#     product_color_size = ProductVariantSerializer(many=True, read_only=True)
#     off_price = serializers.SerializerMethodField()
#     images = serializers.SerializerMethodField()
#
#     class Meta:
#         model = ProductModel
#         fields = ['product',  'price', 'images', 'off_price', 'percent_discount',
#                   'product_code', 'slug', 'created', 'updated', 'product_color_size', 'id']
#
#     def get_off_price(self, obj):
#         price = obj.price
#         percent_discount = obj.percent_discount
#         if obj.percent_discount is None:
#             percent_discount = 0
#         return int(price - price * percent_discount / 100)
#
#     def get_images(self, obj):
#         return {'image1': obj.image1.url,
#                 'image2': obj.image2.url,
#                 'image3': obj.image1.url,
#                 'image4': obj.image1.url,
#                 'image5': obj.image1.url}


class ProductSerializer(serializers.ModelSerializer):
    off_price = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    # size_product = SizeSerializer(many=True, read_only=True)
    size = serializers.SerializerMethodField()

    class Meta:
        model = ProductModel
        fields = ['product',  'price', 'images', 'off_price', 'percent_discount', 'size',
                  'product_code', 'slug', 'created', 'updated', 'id']

    def get_off_price(self, obj):
        price = obj.price
        percent_discount = obj.percent_discount
        if obj.percent_discount is None:
            percent_discount = 0
        return int(price - price * percent_discount / 100)

    def get_images(self, obj):
        return {'image1': obj.image1.url,
                'image2': obj.image2.url,
                'image3': obj.image1.url,
                'image4': obj.image1.url,
                'image5': obj.image1.url}

    def get_size(self, obj):
        product = ProductVariantModel.objects.filter(product=obj)  # .order_by('-priority')
        # size = set([{str(p.size): str(p.size.priority)} for p in product])
        # set([str({str(p.size): str(p.size.priority)})
        sizes = [f"{p.size}: {p.size.priority}" for p in product]
        # return size
        return ", ".join(sizes)


class ColorSizeProductSerializer(serializers.ModelSerializer):
    color = serializers.SlugRelatedField(read_only=True, slug_field='color')
    color_code = serializers.SerializerMethodField()

    class Meta:
        model = ProductVariantModel
        fields = ['color', 'quantity', 'id', 'color_code']
    # color = serializers.CharField()
    # quantity = serializers.IntegerField()
    # id = serializers.IntegerField(read_only=True)

    def get_color_code(self, obj):
        return obj.color.color_code


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
    category = serializers.SlugRelatedField(slug_field='category', read_only=True)

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
