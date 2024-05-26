from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ProductCategoryModel, PopularProductModel, ProductModel, ColorProductModel, ProductVariantModel, \
    SizeProductModel, AddImageGalleryModel, AddCategoryModel, ProductGenderModel
from .serializers import (ProductGenderSerializer, PopularProductSerializer, ProductSerializer, ProductListSerializer,\
    ColorSizeProductSerializer, ProductSearchSerializer, ProductVariantShopSerializer, ProductColorImageSerializer)
from django.shortcuts import get_object_or_404
from rest_framework import status
from .service import Cart
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
import math
import urllib.parse


class ProductCategoryView(APIView):

    def get(self, request):
        gender_category = ProductGenderModel.objects.filter(gender__in=['men', 'women'])
        ser_gender_category = ProductGenderSerializer(instance=gender_category, many=True)

        return Response(data=ser_gender_category.data)


class PopularProductView(APIView):
    def get(self, request):
        popular_product = PopularProductModel.objects.all()
        ser_popular_product = PopularProductSerializer(instance=popular_product, many=True)

        return Response(data=ser_popular_product.data)


class ProductView(APIView):
    def get(self, request):
        product_slug = self.request.query_params.get('slug', None)
        if product_slug is not None:
            product = get_object_or_404(ProductModel, slug=product_slug)
            ser_product = ProductSerializer(instance=product)
            return Response(data=ser_product.data)
        else:
            return Response(data={'massage': 'invalid data'}, status=status.HTTP_400_BAD_REQUEST)


class ProductVariantShopView(APIView):
    """
    note: get product variant price
    queries:
    1. product
    2. size
    3. color
    """
    def get(self, request):
        product_name = self.request.query_params.get('product', None)
        product_size = self.request.query_params.get('size', None)
        product_color = self.request.query_params.get('color', None)
        if product_name is not None and product_size is not None and product_color is not None:
            product_name = ProductModel.objects.get(product=product_name)
            product_size = SizeProductModel.objects.get(size=product_size)
            product_color = ColorProductModel.objects.get(color=product_color)
            product = get_object_or_404(ProductVariantModel, product=product_name, size=product_size, color=product_color)
            ser_product = ProductVariantShopSerializer(instance=product)
            return Response(data=ser_product.data)
        else:
            return Response(data={'massage': 'invalid data'}, status=status.HTTP_400_BAD_REQUEST)


class ProductColorImageView(APIView):
    """
    queryset:
    1. product
    2. color
    """
    def get(self, request):
        product = self.request.query_params.get('product', None)
        product = ProductModel.objects.get(product=product)

        color = self.request.query_params.get('color', None)
        product_color = ColorProductModel.objects.get(color=color)

        images = AddImageGalleryModel.objects.filter(product=product, color=product_color)
        ser_data = ProductColorImageSerializer(many=True, instance=images)
        return Response(data=ser_data.data)


class ColorSizeProductView(APIView):
    def get(self, request):
        product_size = self.request.query_params.get('size', None)
        product_slug = self.request.query_params.get('slug', None)

        product = ProductModel.objects.get(slug=product_slug)
        size = SizeProductModel.objects.get(size=product_size)
        color = product.product_color_size.filter(size=size, quantity__gt=0)
        ser_data = ColorSizeProductSerializer(instance=color, many=True)

        return Response(data=ser_data.data)


class CartView(APIView):
    def get(self, request, format=None):
        cart = Cart(request)


        return Response(
            {"data": list(cart.__iter__()),
             "cart_total_price": cart.get_total_price()},
            status=status.HTTP_200_OK
            )

    def post(self, request, **kwargs):
        """
        parameters:
        1. product # course id
            - id
            - off_price
        2. quantity # product order
        3. remove # true
        4. clear # true
        """

        cart = Cart(request)
        if "remove" in request.data:
            product = request.data["product"]
            cart.remove(product)

            return Response(
                {"message": 'cart removed'},
                status=status.HTTP_202_ACCEPTED)

        elif "clear" in request.data:
            cart.clear()

            return Response(
                {"message": 'cart cleaned'},
                status=status.HTTP_202_ACCEPTED)

        else:
            product = request.data
            add = cart.add(
                product=product["product"],
                quantity=product["quantity"],
                overide_quantity=product["overide_quantity"] if "overide_quantity" in product else False
            )

            return Response(
                {"message": add['massage']},
                status=status.HTTP_202_ACCEPTED)


class ProductListView(APIView):
    def get(self, request):
        """
        get parameter:
        1. page_number
        2. slug
        """

        page_number = int(self.request.query_params.get('page_number', None))
        gender_slug = self.request.query_params.get('slug', None)

        # category = ProductCategoryModel.objects.get(slug=category_slug)
        gender = get_object_or_404(ProductGenderModel, slug=gender_slug)
        unisex = get_object_or_404(ProductGenderModel, slug='unisex')

        per_page = 16

        products_count = len(ProductModel.objects.filter(gender__in=[gender, unisex]))

        # # print(products_count)
        # # products_count = len(ProductModel.objects.filter(category=category))
        number_of_pages = math.ceil(products_count/per_page)
        if page_number is not None:
            product_list = ProductModel.objects.filter(gender__in=[gender, unisex]).order_by('-priority')[per_page*(page_number-1):per_page*page_number]
        else:
            product_list = ProductModel.objects.filter(gender__in=[gender, unisex]).order_by('-priority')

        ser_product_list = ProductListSerializer(instance=product_list, many=True)
        category_title = gender.gender
        #
        return Response(data={'data': ser_product_list.data, 'title': category_title, 'number_of_pages': number_of_pages})
        # return Response(data={'data': 'ser_product_list.data'})


class SearchProductView(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSearchSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['date']
    # filterset_class = PdfFilter
    search_fields = ['product']
    # search_fields = ['date', 'date_paper__paper_category__title']
    ordering_fields = '__all__'


class SizeOfColorView(APIView):
    def get(self, request):
        product_query = self.request.query_params.get('product', None)
        # if product_query:
        #     product_query = urllib.parse.unquote(product_query)  # Decode the product name
        # print(product_query)

        product = ProductModel.objects.get(product=product_query)

        color_query = self.request.query_params.get('color', None)
        color = ColorProductModel.objects.get(color=color_query)

        products = ProductVariantModel.objects.filter(product=product, color=color, quantity__gt=0)
        sizes = []
        for product in products:
            sizes.append(product.size.size)
        print(sizes)
        return Response(data=sizes)
