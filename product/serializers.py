from rest_framework import serializers
from .models import ProductCategoryModel, PopularProductModel, ProductModel, ProductVariantModel, ColorProductModel,\
    SizeProductModel, ProductSubCategoryModel, AddImageGalleryModel, AddCategoryModel, ProductGenderModel


class ProductGenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGenderModel
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
#                   'group_id', 'slug', 'created', 'updated', 'product_color_size', 'id']
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
    # off_price = serializers.SerializerMethodField()
    # images = serializers.SerializerMethodField()
    # size_product = SizeSerializer(many=True, read_only=True)
    colors = serializers.SerializerMethodField()
    all_size = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    subcategory = serializers.SerializerMethodField()
    gender = serializers.SlugRelatedField(read_only=True, slug_field='gender')

    class Meta:
        model = ProductModel
        fields = ['product', 'percent_discount', 'colors', 'all_size', 'size', 'cover_image', 'size_table_image',
                  'description_image', 'application_fields', 'descriptions', 'category', 'subcategory', 'gender',
                  'group_id', 'slug', 'created', 'updated', 'id', 'price']

    def get_category(self, obj):
        categories = obj.category_product.all()
        categories = [category.category.category for category in categories]
        return categories

    def get_subcategory(self, obj):
        subcategories = obj.subcategory_product.all()
        subcategories = [subcategory.subcategory.subcategory for subcategory in subcategories]
        return subcategories


    # def get_off_price(self, obj):
    #     price = obj.price
    #     percent_discount = obj.percent_discount
    #     if obj.percent_discount is None:
    #         percent_discount = 0
    #     return int(price - price * percent_discount / 100)

    # def get_images(self, obj):
    #     image1 = obj.image1.url if obj.image1 else None
    #     image2 = obj.image2.url if obj.image2 else None
    #     image3 = obj.image3.url if obj.image3 else None
    #     image4 = obj.image4.url if obj.image4 else None
    #     image5 = obj.image5.url if obj.image5 else None
    #
    #     return {'image1': image1,
    #             'image2': image2,
    #             'image3': image3,
    #             'image4': image4,
    #             'image5': image5}

    def get_colors(self, obj):
        product = ProductVariantModel.objects.filter(product=obj)

        colors = set([f'{str(p.color.color)} - {str(p.color.color_code)}' for p in product])
        # colors = sorted(colors, key=lambda x: int(x.split(" - ")[1]))
        all_colors = [{'color': color.split(" - ")[0], 'code': color.split(" - ")[1]} for color in colors]
        return all_colors

    def get_all_size(self, obj):
        product = ProductVariantModel.objects.filter(product=obj)  # .order_by('-priority')
        # product = product.objects.filter(quantity__gt=0)
        # size = set([str(p.size) for p in product])
        size = set([f'{str(p.size)} - {str(p.size.priority)}' for p in product])
        sizes = sorted(size, key=lambda x: int(x.split(" - ")[1]))
        all_size = [size.split(" - ")[0] for size in sizes]
        return all_size

    def get_size(self, obj):
        product = ProductVariantModel.objects.filter(product=obj)  # .order_by('-priority')
        # product = product.objects.filter(quantity__gt=0)
        # size = set([str(p.size) for p in product])
        size = set([f'{str(p.size)} - {str(p.size.priority)}' for p in product if p.quantity > 0])
        sizes = sorted(size, key=lambda x: int(x.split(" - ")[1]))
        size = [size.split(" - ")[0] for size in sizes]
        return size


# class ProductSerializer(serializers.ModelSerializer):
#     product = serializers.SlugRelatedField(read_only=True, slug_field='product')
#     size = serializers.SlugRelatedField(read_only=True, slug_field='size')
#     color = serializers.SlugRelatedField(read_only=True, slug_field='color')
#     off_price = serializers.SerializerMethodField()
#     images = serializers.SerializerMethodField()
#     size_products = serializers.SerializerMethodField()
#
#     class Meta:
#         model = ProductVariantModel
#         fields = ['product',  'price', 'off_price', 'images', 'percent_discount', 'size_products', 'size', 'color',
#                   'item_id', 'slug', 'created', 'updated', 'id']
#
#     def get_images(self, obj):
#         obj = obj.product
#         image1 = obj.image1.url if obj.image1 else None
#         image2 = obj.image2.url if obj.image2 else None
#         image3 = obj.image3.url if obj.image3 else None
#         image4 = obj.image4.url if obj.image4 else None
#         image5 = obj.image5.url if obj.image5 else None
#
#         return {'image1': image1,
#                 'image2': image2,
#                 'image3': image3,
#                 'image4': image4,
#                 'image5': image5}
#
#     def get_size_products(self, obj):
#         obj = obj.product
#         product = ProductVariantModel.objects.filter(product=obj)  # .order_by('-priority')
#         # size = set([str(p.size) for p in product])
#         size = set([f'{str(p.size)} - {str(p.size.priority)}' for p in product])
#         sizes = sorted(size, key=lambda x: int(x.split(" - ")[1]))
#         size = [size.split(" - ")[0] for size in sizes]
#         return size
#
#     def get_off_price(self, obj):
#         price = obj.price
#         percent_discount = obj.percent_discount
#         if obj.percent_discount is None:
#             percent_discount = 0
#         return int(price - price * percent_discount / 100)


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
        fields = ['id', 'product', 'image1', 'price', 'off_price', 'slug', 'product_color_size', 'group_id']

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
    gender = serializers.SlugRelatedField(slug_field='gender', read_only=True)
    # product = serializers.SlugRelatedField(slug_field='product', read_only=True)
    category = serializers.SerializerMethodField()
    subcategory = serializers.SerializerMethodField()
    # cover = serializers.SerializerMethodField()
    # price = serializers.SerializerMethodField()
    off_price = serializers.SerializerMethodField()
    # percent_discount = serializers.SerializerMethodField()
    # slug = serializers.SerializerMethodField()
    # group_id = serializers.SerializerMethodField()

    class Meta:
        model = ProductModel
        fields = ['gender', 'category', 'subcategory', 'product', 'cover_image', 'price', 'off_price',
                  'percent_discount', 'group_id', 'slug', 'subtitle']
        # fields = ['category', 'subcategory', 'product', 'cover', 'price', 'off_price', 'percent_discount',
        #           'group_id', 'slug']

    def get_category(self, obj):
        categories = obj.category_product.all()
        categories = [category.category.category for category in categories]

        return categories

    def get_subcategory(self, obj):
        subcategories = obj.subcategory_product.all()
        subcategories = [subcategory.subcategory.subcategory for subcategory in subcategories]

        return subcategories

    # def get_slug(self, obj):
    #     product_name = obj
    #     slug = product_name.product.slug
    #     # product = ProductModel.objects.get(product=product_name)
    #     # subcategories = product.subcategory_product.all()
    #     # subcategory_list = [subcategory.subcategory.subcategory for subcategory in subcategories]
    #     return slug

    # def get_group_id(self, obj):
    #     product_name = obj
    #     group_id = product_name.product.group_id
    #     # product = ProductModel.objects.get(product=product_name)
    #     # subcategories = product.subcategory_product.all()
    #     # subcategory_list = [subcategory.subcategory.subcategory for subcategory in subcategories]
    #     return group_id

    # def get_percent_discount(self, obj):
    #     product_name = obj
    #     percent_discount = product_name.product.percent_discount
    #     # product = ProductModel.objects.get(product=product_name)
    #     # subcategories = product.subcategory_product.all()
    #     # subcategory_list = [subcategory.subcategory.subcategory for subcategory in subcategories]
    #     return percent_discount

    # def get_off_price(self, obj):
    #     product_name = obj
    #     price = product_name.product.price
    #     percent_discount = product_name.product.percent_discount
    #     if percent_discount is None:
    #         percent_discount = 0
    #     return int(price - price * percent_discount / 100)

    # def get_price(self, obj):
    #     product_name = obj
    #     price = product_name.product.price
    #     return price

    # def get_cover(self, obj):
    #     product_name = obj
    #     cover = product_name.product.cover_image.url
    #     print(cover)
    #     # product = ProductModel.objects.get(product=product_name)
    #     # subcategories = product.subcategory_product.all()
    #     # subcategory_list = [subcategory.subcategory.subcategory for subcategory in subcategories]
    #     return cover


    # def get_subcategory(self, obj):
    #     product_name = obj
    #     product = ProductModel.objects.get(product=product_name)
    #     subcategories = product.subcategory_product.all()
    #     subcategory_list = [subcategory.subcategory.subcategory for subcategory in subcategories]
    #     return subcategory_list
    #
    def get_off_price(self, obj):
        price = obj.price
        percent_discount = obj.percent_discount
        if obj.percent_discount is None:
            percent_discount = 0
        return int(price - price * percent_discount / 100)


class ProductSearchSerializer(serializers.ModelSerializer):
    off_price = serializers.SerializerMethodField()

    class Meta:
        model = ProductModel
        fields = ['product', 'price', 'off_price', 'slug', 'group_id', 'id']

    def get_off_price(self, obj):
        price = obj.price
        percent_discount = obj.percent_discount
        if obj.percent_discount is None:
            percent_discount = 0
        return int(price - price * percent_discount / 100)


class ProductVariantShopSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(read_only=True, slug_field='product')
    size = serializers.SlugRelatedField(read_only=True, slug_field='size')
    color = serializers.SlugRelatedField(read_only=True, slug_field='color')
    off_price = serializers.SerializerMethodField()

    class Meta:
        model = ProductVariantModel
        fields = ['product', 'name', 'price', 'off_price', 'percent_discount',
                  'quantity', 'size', 'color', 'item_id', 'slug', 'id']

    def get_off_price(self, obj):
        price = obj.price
        percent_discount = obj.percent_discount
        if obj.percent_discount is None:
            percent_discount = 0
        return int(price - price * percent_discount / 100)


class ProductColorImageSerializer(serializers.ModelSerializer):
    # images = serializers.SerializerMethodField()
    class Meta:
        model = AddImageGalleryModel
        fields = ['image']

    # def get_images(self, obj):
    #     images = obj.image
    #     print(images)
    #     return images
