from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from product.models import ProductModel, ProductCategoryModel
from .serializers import ProductSerializer, CategorySerializer


class ProductView(APIView):
    def get(self, request):
        products = ProductModel.objects.all()
        ser_data = ProductSerializer(instance=products, many=True)
        return Response(data=ser_data.data)


class CategoryView(APIView):
    def get(self, request):
        category = ProductCategoryModel.objects.all()
        ser_data = CategorySerializer(instance=category, many=True)
        return Response(data=ser_data.data)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request, id_category):
        try:
            category = ProductCategoryModel.objects.get(id=id_category)
        except:
            return Response(data={'message': 'Category is not exist'})

        name = category.category
        category.delete()
        return Response(data={'message': f'The {name} category was deleted'})
