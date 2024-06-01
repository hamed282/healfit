from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import ProductModel
from .serializers import ProductSerializer


class ProductView(APIView):
    def get(self, request):
        products = ProductModel.objects.all()
        ser_data = ProductSerializer(instance=products, many=True)
        return Response(data=ser_data.data)
