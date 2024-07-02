from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from product.models import (ProductModel, ProductCategoryModel, ExtraGroupModel, ColorProductModel, SizeProductModel,
                            AddCategoryModel, AddSubCategoryModel, ProductSubCategoryModel)
from accounts.models import User
from .serializers import (ProductSerializer, CategorySerializer, LoginUserSerializer, ExtraGroupSerializer,
                          AddCategorySerializer, AddImageGallerySerializer)
from accounts.serializers import UserLoginSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


class ProductView(APIView):
    def get(self, request):
        products = ProductModel.objects.all()
        ser_data = ProductSerializer(instance=products, many=True)
        return Response(data=ser_data.data)

    def post(self, request):
        form = request.data
        ser_data = AddImageGallerySerializer(data=form)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
        # ser_data = ProductSerializer(data=form)
        # if ser_data.is_valid():
        #     ser_data.save()
        #     return Response(ser_data.data, status=status.HTTP_201_CREATED)
        # return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

        # form_product = request.data.get('product')
        # form_category = request.data.get('category')
        # form_subcategory = request.data.get('subcategory')
        # print(form_category)
        # product_serializer = ProductSerializer(data=form_product)
        # # category_serializer = AddCategorySerializer(data=form_category)
        # print('t' * 100)
        #
        # if product_serializer.is_valid():
        #
        #     product = product_serializer.save()
        #
        #     for cat in form_category:
        #         category = ProductCategoryModel.objects.get(category=cat)
        #         add_category = AddCategoryModel(category=category,
        #                                         product=product)
        #         add_category.save()
        #
        #     for sub in form_subcategory:
        #         subcategory = ProductSubCategoryModel.objects.get(subcategory=sub)
        #         add_subcategory = AddSubCategoryModel(subcategory=subcategory,
        #                                               product=product)
        #         add_subcategory.save()
        #
        #     response_data = {
        #         'product': product_serializer.data,
        #         # 'category': category_serializer.data,
        #     }
        #     return Response(response_data, status=status.HTTP_201_CREATED)
        #
        # errors = {}
        # if not product_serializer.is_valid():
        #     errors['product'] = product_serializer.errors
        # return Response(errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryView(APIView):
    def get(self, request):
        category = ProductCategoryModel.objects.all()
        ser_data = CategorySerializer(instance=category, many=True)
        return Response(data=ser_data.data)

    def post(self, request):
        form = request.data

        ser_data = CategorySerializer(data=form)
        if ser_data.is_valid():
            ser_data.save()

            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        id_category = self.request.query_params.get('id_category', None)

        if id_category is None:
            return Response(data={'message': 'Input category ID'})

        try:
            category = ProductCategoryModel.objects.get(id=id_category)
        except:
            return Response(data={'message': 'Category is not exist'})

        ser_data = CategorySerializer(instance=category, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data, status=status.HTTP_200_OK)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

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


class CategoryItemView(APIView):
    def get(self, request, category_id):

        category = get_object_or_404(ProductCategoryModel, id=category_id)
        ser_data = CategorySerializer(instance=category)
        return Response(data=ser_data.data)


class CategorySearchView(APIView):
    def get(self, request):
        print('-'*100)
        category = self.request.query_params.get('search')
        print('7777')
        category = ProductCategoryModel.objects.filter(category=category)
        ser_data = CategorySerializer(instance=category, many=True)
        return Response(data=ser_data.data)


class ExtraGroupView(APIView):
    def get(self, request):
        extr_group = ExtraGroupModel.objects.all()
        ser_data = ExtraGroupSerializer(instance=extr_group, many=True)
        return Response(data=ser_data.data)

    def post(self, request):
        form = request.data

        ser_data = ExtraGroupSerializer(data=form)

        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        id_extrag = self.request.query_params.get('id_extrag', None)

        if id_extrag is None:
            return Response(data={'message': 'Input Extra Group ID'})

        try:
            extrag = ExtraGroupModel.objects.get(id=id_extrag)
        except:
            return Response(data={'message': 'Extra Group is not exist'})

        ser_data = ExtraGroupSerializer(instance=extrag, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data, status=status.HTTP_200_OK)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        id_extrag = self.request.query_params.get('id_extrag', None)

        if id_extrag is None:
            return Response(data={'message': 'Input Extra Group ID'})

        try:
            extrag = ExtraGroupModel.objects.get(id=id_extrag)
        except:
            return Response(data={'message': 'Extra Group is not exist'})

        name = extrag.title
        extrag.delete()
        return Response(data={'message': f'The {name} Extra Group was deleted'})


# class ExtraValueView(APIView):
#     def get(self, request):
#         extr_size = SizeProductModel.objects.all()
#         extr_color = ColorProductModel.objects.all()
#
#         ser_data = ExtraGroupSerializer(instance=extr_group, many=True)
#         return Response(data=ser_data.data)


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
