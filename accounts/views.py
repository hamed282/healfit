from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, AddressModel
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserAddressSerializer, UserInfoSerializer,\
    UserInfoChangeSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
import requests
import json


class UserRegisterView(APIView):

    def post(self, request):
        """
        parameters:
        1. first_name
        2. last_name
        3. email
        4. phone_number
        5. password
        """
        form = request.data
        ser_data = UserRegisterSerializer(data=form)
        if ser_data.is_valid():
            user = User.objects.filter(email=form['email']).exists()
            if not user:
                User.objects.create_user(first_name=form['first_name'],
                                         last_name=form['last_name'],
                                         email=form['email'],
                                         phone_number=form['phone_number'],
                                         password=form['password'])
                try:
                    user = authenticate(email=form['email'], password=form['password'])
                    if user is not None:
                        user = User.objects.get(email=form['email'])
                        if user.is_active:
                            token_access = AccessToken.for_user(user)
                            token_refresh = RefreshToken.for_user(user)
                            return Response(data={'access': str(token_access), 'refresh': str(token_refresh)},
                                            status=status.HTTP_201_CREATED)
                        return Response(data='user is not active', status=status.HTTP_401_UNAUTHORIZED)
                    else:
                        return Response(data='user invalid', status=status.HTTP_401_UNAUTHORIZED)
                except:
                    user = None
            else:
                return Response(data={'message': 'user with this Email already exists.'},
                                status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(data=ser_data.errors, status=status.HTTP_401_UNAUTHORIZED)


class UserLoginView(APIView):

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
                    if user.is_active:
                        token_access = AccessToken.for_user(user)
                        token_refresh = RefreshToken.for_user(user)
                        return Response(data={'access': str(token_access), 'refresh': str(token_refresh)},
                                        status=status.HTTP_200_OK)
                    return Response(data='user is not active', status=status.HTTP_401_UNAUTHORIZED)
                else:
                    return Response(data='user invalid', status=status.HTTP_401_UNAUTHORIZED)
            except:
                user = None

        return Response(data=ser_data.errors, status=status.HTTP_401_UNAUTHORIZED)


class UserLogout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        parameters:
        1. refresh_token

        sample: {"refresh_token": "dsade3ewqdwxr44354x4rxexrre"}
        """
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserAddressView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        addresses = AddressModel.objects.filter(user=request.user)
        ser_addresses = UserAddressSerializer(instance=addresses, many=True)
        return Response(data=ser_addresses.data)

    def post(self, request):
        """
        parameters:
        {
            address
            additional_information
            emirats
            city
            country
        }
        """
        form = request.data
        ser_address = UserAddressSerializer(data=form)
        if ser_address.is_valid():
            address = AddressModel.objects.create(user=request.user,
                                                  address=form['address'],
                                                  additional_information=form['additional_information'],
                                                  emirats=form['emirats'],
                                                  city=form['city'],
                                                  country=form['country'])
            # address.save()
            return Response(data={'massage': 'Address added'}, status=status.HTTP_201_CREATED)
        else:
            return Response(data=ser_address.errors, status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request):
        address_id = self.request.query_params.get('address_id', None)
        address = get_object_or_404(AddressModel, id=address_id)
        if address.user.id == request.user.id:
            form = request.data

            ser_address = UserAddressSerializer(instance=address, data=form, partial=True)
            if ser_address.is_valid():
                ser_address.save()
                return Response(data=ser_address.data, status=status.HTTP_200_OK)
            return Response(data=ser_address.errors, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        address_id = self.request.query_params.get('address_id', None)
        address = get_object_or_404(AddressModel, id=address_id)
        if address_id is not None:
            if address.user.id == request.user.id:

                address = AddressModel.objects.get(id=address_id)
                address.delete()
                return Response(data={'massage': 'address deleted'}, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.user.id
        user_info = get_object_or_404(User, id=user_id)
        if user_info.id == request.user.id:
            ser_user_info = UserInfoSerializer(instance=user_info)
        else:
            ser_user_info = None
        return Response(data=ser_user_info.data)

    def put(self, request):
        """
        parameters:
        1. first_name
        2. last_name
        3. emai
        4. phone_number
        5. password
        """
        user_info = get_object_or_404(User, id=request.user.id)
        if user_info.id == request.user.id:
            form = request.data

            ser_user_info = UserInfoChangeSerializer(instance=user_info, data=form, partial=True)
            if ser_user_info.is_valid():
                ser_user_info.save()
                return Response(data={'message': 'Done'}, status=status.HTTP_200_OK)
            return Response(data=ser_user_info.errors, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# class GoogleView(APIView):
#     def post(self, request):
#         payload = {'access_token': request.data.get("token")}  # validate the token
#         r = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
#         data = json.loads(r.text)
#
#         if 'error' in data:
#             content = {'message': 'wrong google token / this google token is already expired.'}
#             return Response(content)
#
#         # create user if not exist
#         try:
#             user = User.objects.get(email=data['email'])
#         except User.DoesNotExist:
#             user = User()
#             user.email = data['email']
#             # provider random default password
#             user.password = make_password(BaseUserManager().make_random_password())
#             user.save()
#
#         token = RefreshToken.for_user(user)  # generate token without username & password
#         response = {}
#         response['username'] = user.username
#         response['access_token'] = str(token.access_token)
#         response['refresh_token'] = str(token)
#         return Response(response)
