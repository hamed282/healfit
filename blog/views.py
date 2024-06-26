from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import BlogModel
from .serializers import BlogSerializer, BlogAllSerializer
import math


class BLogListView(APIView):
    def get(self, request):
        limit = self.request.query_params.get('limit', None)
        page = self.request.query_params.get('page', None)

        per_page = 16
        blog_count = len(BlogModel.objects.all())
        number_of_pages = math.ceil(blog_count / per_page)
        if limit is not None:
            blog = BlogModel.objects.all()[:int(limit)]
            ser_data = BlogAllSerializer(instance=blog, many=True)
            return Response(data=ser_data.data)

        if page is not None:
            page = int(page)
            blog = BlogModel.objects.all()[per_page*(page-1):per_page*page]
        else:
            blog = BlogModel.objects.all()

        ser_data = BlogAllSerializer(instance=blog, many=True)
        return Response({'data': ser_data.data, 'number_of_pages': number_of_pages})


# class BlogLandView(APIView):
#     def get(self, request):
#         blog = BlogModel.objects.all()[:4]
#         ser_data = BlogLandSerializer(instance=blog, many=True)
#         return Response(ser_data.data)


class BlogView(APIView):
    def get(self, request, slug):
        blog = get_object_or_404(BlogModel, slug=slug)
        ser_data = BlogSerializer(instance=blog)
        return Response(data=ser_data.data)


class RelatedPostView(APIView):
    def get(self, request):
        limit = self.request.query_params.get('limit', None)
        category = self.request.query_params.get('category', None)

        if limit is not None:
            blog = BlogModel.objects.filter(category=category)[:int(limit)]
        else:
            blog = BlogModel.objects.filter(category=category)
        ser_data = BlogAllSerializer(instance=blog, many=True)
        return Response(data=ser_data.data)
