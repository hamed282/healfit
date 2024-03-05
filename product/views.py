from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ProductCategoryModel, PopularProductModel, ProductModel, ColorProductModel, ProductVariantModel, SizeProductModel
from .serializers import ProductCategorySerializer, PopularProductSerializer, ProductSerializer, ProductListSerializer, ColorSizeProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from .service import Cart


class ProductCategoryView(APIView):
    # authentication_classes = [JWTAuthentication]

    def get(self, request):
        product_category = ProductCategoryModel.objects.all()
        ser_product_category = ProductCategorySerializer(instance=product_category, many=True)

        return Response(data=ser_product_category.data)


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
        1. limit_from
        2. limit_to
        3. slug
        """
        product_limit_from = self.request.query_params.get('limit_from', None)
        product_limit_to = self.request.query_params.get('limit_to', None)
        product_slug = self.request.query_params.get('slug', None)
        category = ProductCategoryModel.objects.get(slug=product_slug)
        if product_limit_from is None and product_limit_to is None:
            product_list = ProductModel.objects.filter(category=category).order_by('-created')
        elif product_limit_from is not None and product_limit_to is None:
            product_list = ProductModel.objects.all().order_by('-created')[int(product_limit_from):]
        elif product_limit_from is None and product_limit_to is not None:
            product_list = ProductModel.objects.all().order_by('-created')[:int(product_limit_to)]
        else:
            product_list = ProductModel.objects.all().order_by('-created')[int(product_limit_from):int(product_limit_to)]

        ser_product_list = ProductListSerializer(instance=product_list, many=True)
        category_title = category.category_title

        return Response(data={'data': ser_product_list.data, 'title': category_title})
