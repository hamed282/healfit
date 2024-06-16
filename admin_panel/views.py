from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from product.models import ProductModel, ProductCategoryModel
from accounts.models import User
from .serializers import ProductSerializer, CategorySerializer, LoginUserSerializer


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

    def delete(self, request):
        id_category = self.request.query_params.get('id_category', None)

        if id_category is None:
            return Response(data={'message': 'Input category ID'})

        try:
            category = ProductCategoryModel.objects.get(id=id_category)
        except:
            return Response(data={'message': 'Category is not exist'})

        name = category.category
        category.delete()
        return Response(data={'message': f'The {name} category was deleted'})


from accounts.serializers import UserLoginSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


class LoginUserView(APIView):

    def post(self, request):
        """
        parameters:
        1. email
        2. password
        """
        form = request.data
        ser_data = UserLoginSerializer(data=form)
        if ser_data.is_valid():
            try:
                user = authenticate(email=form['email'], password=form['password'])
                if user is not None:
                    user = User.objects.get(email=form['email'])
                    if user.is_admin:
                        token_access = AccessToken.for_user(user)
                        token_refresh = RefreshToken.for_user(user)

                        ser_data = LoginUserSerializer(instance=user)

                        return Response(data={'data': {'access_token': str(token_access),
                                                       'refresh_token': str(token_refresh),
                                                       'token_type': 'Bearer',
                                                       'user': ser_data.data}},
                                        status=status.HTTP_200_OK)
                    return Response(data='user is not active', status=status.HTTP_401_UNAUTHORIZED)
                else:
                    return Response(data='user invalid', status=status.HTTP_401_UNAUTHORIZED)
            except:
                user = None

        return Response(data=ser_data.errors, status=status.HTTP_401_UNAUTHORIZED)
