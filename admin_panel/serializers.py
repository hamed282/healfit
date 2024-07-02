from rest_framework import serializers
from product.models import (ProductModel, ProductCategoryModel, ExtraGroupModel, AddImageGalleryModel, AddCategoryModel,
                            AddSubCategoryModel, ColorProductModel, SizeProductModel)
from accounts.models import User


class ProductSerializer(serializers.ModelSerializer):
    gender = serializers.SlugRelatedField(read_only=True, slug_field='gender')
    image_gallery = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField(read_only=False)
    subcategory = serializers.SerializerMethodField()

    class Meta:
        model = ProductModel
        fields = '__all__'

    def get_image_gallery(self, product):
        image_gallery = AddImageGalleryModel.objects.filter(product=product)
        images = [{'color': f'{image.color.color}', 'image': f'{image.image.url}'} for image in image_gallery]
        return images

    def get_category(self, product):
        categories = AddCategoryModel.objects.filter(product=product)
        category = [category.category.category for category in categories]
        return category

    def get_subcategory(self, product):
        subcategories = AddSubCategoryModel.objects.filter(product=product)
        subcategory = [subcategory.subcategory.subcategory for subcategory in subcategories]
        return subcategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategoryModel
        fields = '__all__'


class AddCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddCategoryModel
        fields = '__all__'


class AddImageGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddImageGalleryModel
        fields = '__all__'


class ColorValueSerializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    class Meta:
        model = ColorProductModel
        fields = ['value', 'type', 'title']

    def get_value(self, obj):
        value = obj.color_code
        return value

    def get_type(self, obj):
        return 'color'

    def get_title(self, obj):
        title = obj.color
        return title


class ExtraGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraGroupModel
        fields = '__all__'


class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']
