from rest_framework.views import APIView
from rest_framework.response import Response


class BlogView(APIView):
    def get(self, request):
        return Response(data='data')


