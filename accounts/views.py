from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, AddressModel
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserAddressSerializer, UserInfoSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404


class UserRegisterView(APIView):

    def post(self, request):
        """
        parameters:
        1. first_name
        2. last_name
        3. email
        4. birthdate
        5. password
        """
        form = request.data
        ser_data = UserRegisterSerializer(data=form)
        if ser_data.is_valid():
            user = User.objects.filter(email=form['email']).exists()
            if not user:
                User.objects.create_user(first_name=form['first_name'],
                                         last_name=form['last_name'],
                                         email=form['email'], birthdate=form['birthdate'],
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
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserAddressView(APIView):
    def get(self, request):
        addresses = AddressModel.objects.filter(user=request.user)
        ser_addresses = UserAddressSerializer(instance=addresses, many=True)
        return Response(data=ser_addresses.data)

    def post(self, request):
        """
        parameters:
        {
            first_name_address
            last_name_address
            company
            VAT_number
            address
            address_complement
            phone_number
            postal_code
            city
            country
            identification_number
        }
        """
        form = request.data
        ser_address = UserAddressSerializer(data=form)
        if ser_address.is_valid():
            address = AddressModel.objects.create(user=request.user,
                                                  first_name_address=form['first_name_address'],
                                                  last_name_address=form['last_name_address'],
                                                  company=form['company'],
                                                  VAT_number=form['VAT_number'],
                                                  address=form['address'],
                                                  address_complement=form['address_complement'],
                                                  phone_number=form['phone_number'],
                                                  postal_code=form['postal_code'],
                                                  city=form['city'],
                                                  country=form['country'],
                                                  identification_number=form['identification_number'])
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
    def get(self, request):
        user_id = request.user.id
        user_info = get_object_or_404(User, id=user_id)
        if user_info.id == request.user.id:
            ser_user_info = UserInfoSerializer(instance=user_info)
        else:
            ser_user_info = None
        return Response(data=ser_user_info.data)

    def put(self, request):
        user_info = get_object_or_404(User, id=request.user.id)
        if user_info.id == request.user.id:
            form = request.data

            ser_user_info = UserAddressSerializer(instance=user_info, data=form, partial=True)
            if ser_user_info.is_valid():
                ser_user_info.save()
                return Response(data=ser_user_info.data, status=status.HTTP_200_OK)
            return Response(data=ser_user_info.errors, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
