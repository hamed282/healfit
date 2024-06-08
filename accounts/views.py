from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, AddressModel
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserAddressSerializer, UserInfoSerializer,\
    UserInfoChangeSerializer, ChangePasswordSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import  AccessToken
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import update_session_auth_hash
from django.conf import settings
import requests
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from datetime import datetime, timedelta

class UserRegisterView(APIView):

    def post(self, request):
        """
        parameters:
        1. first_name
        2. last_name
        3. email
        4. phone_number
        5. trn_number
        6. company_name
        7. password
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
                                         trn_number=form['trn_number'],
                                         company_name=form['company_name'],
                                         password=form['password']),
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
            return Response(data='Logout successfully', status=status.HTTP_205_RESET_CONTENT)
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
            phone_number
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
                                                  country=form['country'],
                                                  phone_number=form['phone_number'])
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


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        parameters:
        1. old_password
        2. new_password
        """
        ser_data = ChangePasswordSerializer(data=request.data)
        if ser_data.is_valid():
            user = request.user
            if user.check_password(ser_data.data.get('old_password')):
                user.set_password(ser_data.data.get('new_password'))
                user.save()
                update_session_auth_hash(request, user)  # To update session after password change
                return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
            return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


"""
send link: http://localhost:8000/api/password_reset/   {"email": "your_email@example.com"}

http://localhost:8000/api/password_reset/confirm/
POST
{"password":"Password@123", "token": "60d9dd6559500cc469"}
"""

# class RestPasswordView(APIView):
#
#     def post(self, request):
#         """
#         parameters:
#         1. password
#         2. Token
#         """
#         user = request.user
#
#         ser_data = ResetPasswordSerializer(data=request.data)
#         if ser_data.is_valid():
#             pass

# def change_password(request):
#     if request.method == 'POST':
#         serializer = ChangePasswordSerializer(data=request.data)
#         if serializer.is_valid():
#             user = request.user
#             if user.check_password(serializer.data.get('old_password')):
#                 user.set_password(serializer.data.get('new_password'))
#                 user.save()
#                 update_session_auth_hash(request, user)  # To update session after password change
#                 return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
#             return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class GoogleLoginView(APIView):

    def post(self, request):

        code = request.data.get('code')
        token_url = "https://oauth2.googleapis.com/token"
        token_data = {
            'code': code,
            'client_id': settings.GOOGLE_CLIENT_ID,
            'client_secret': settings.GOOGLE_CLIENT_SECRET,
            'redirect_uri': settings.GOOGLE_REDIRECT_URI,
            'grant_type': 'authorization_code'
        }
        token_response = requests.post(token_url, data=token_data)
        token_json = token_response.json()

        access_token = token_json.get('access_token')
        user_info_url = "https://www.googleapis.com/oauth2/v1/userinfo"
        user_info_params = {'access_token': access_token}
        user_info_response = requests.get(user_info_url, params=user_info_params)
        user_info = user_info_response.json()

        email = user_info.get('email')
        print('-'*100)
        name = user_info.get('name')

        user, created = User.objects.get_or_create(email=email)
        print('#' * 100)
        refresh = RefreshToken.for_user(user)
        tokens = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return Response(tokens, status=status.HTTP_200_OK)


# class GoogleLoginLink(APIView):
#     def get(self, requesr):
#         link = (f'https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={settings.GOOGLE_CLIENT_ID}'
#                 f'&redirect_uri={settings.GOOGLE_REDIRECT_URI}&scope=email%20profile&access_type=online')
#         return Response(data={'redirect_to': link})


class AppleLoginView(APIView):

    def post(self, request):
        id_token = request.data.get('id_token')
        client_secret = self.generate_client_secret()

        # Verify the ID token with Apple
        headers = {
            'kid': settings.APPLE_KEY_ID,
            'alg': 'ES256'
        }
        audience = settings.APPLE_CLIENT_ID
        claims = jwt.decode(id_token, verify=False)

        if claims['aud'] != audience:
            return Response({'error': 'Invalid audience'}, status=status.HTTP_400_BAD_REQUEST)

        email = claims.get('email')
        name = claims.get('name', '')

        user, created = User.objects.get_or_create(email=email, defaults={'name': name})

        refresh = RefreshToken.for_user(user)
        tokens = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return Response(tokens, status=status.HTTP_200_OK)

    def generate_client_secret(self):
        headers = {
            'alg': 'ES256',
            'kid': settings.APPLE_KEY_ID
        }
        payload = {
            'iss': settings.APPLE_TEAM_ID,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(days=180),
            'aud': 'https://appleid.apple.com',
            'sub': settings.APPLE_CLIENT_ID
        }
        client_secret = jwt.encode(payload, settings.APPLE_PRIVATE_KEY, algorithm='ES256', headers=headers)
        return client_secret
