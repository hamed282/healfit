from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MiddleBannerSliderModel, HomeSettingModel, ContactModel, ProductSettingModel, CartSettingModel,\
    BannerHomeModel, ContactSubmitModel
from .serializers import ContactSerializer, HomeSettingSerializer, MiddleBannerSliderSerializer,\
    ProductSettingSerializer, CartSettingSerializer, BannerHomeSerializer, ContactSubmitSerializer
from django.conf import settings
from django.core.mail import send_mail
from product import tasks


class HomeView(APIView):
    def get(self, request):
        setting_home = HomeSettingModel.objects.all()
        ser_setting_home = HomeSettingSerializer(instance=setting_home, many=True)
        return Response(data={'home': ser_setting_home.data})


class SocialMediaView(APIView):
    def get(self, request):
        social_media = ContactModel.objects.all()
        ser_social_media = ContactSerializer(instance=social_media, many=True)

        return Response(data={'contact': ser_social_media.data})


class MiddleBannerSliderView(APIView):
    def get(self, request):
        banner_slider = MiddleBannerSliderModel.objects.all()
        ser_banner_slider = MiddleBannerSliderSerializer(instance=banner_slider, many=True)

        return Response(data={'middle_slider': ser_banner_slider.data})


class HomeSliderView(APIView):
    def get(self, request):
        banner_slider = BannerHomeModel.objects.all()
        ser_banner_slider = BannerHomeSerializer(instance=banner_slider, many=True)

        return Response(data={'home_slider': ser_banner_slider.data})


class ProductSettingView(APIView):
    def get(self, request):
        product_setting = ProductSettingModel.objects.all()
        ser_product_setting = ProductSettingSerializer(instance=product_setting, many=True)

        return Response(data={'product_setting': ser_product_setting.data})


class CartSettingView(APIView):
    def get(self, request):
        product_cart = CartSettingModel.objects.all()
        ser_product_cart = CartSettingSerializer(instance=product_cart, many=True)

        return Response(data={'product_cart': ser_product_cart.data})


class SessionIdView(APIView):
    def get(self, request):
        session_id = request.session.session_key
        if session_id is None:
            request.session['create_session'] = 'create'
            request.session.save()
            session_id = request.session.session_key
        return Response(data={'sessionId': session_id})


class ContactView(APIView):
    def post(self, request):
        """
        parameters:
        1. first_name
        2. last_name
        3. email
        4. mobile
        5. message
        """
        form = request.data
        ser_submit = ContactSubmitSerializer(data=form)
        if ser_submit.is_valid():
            ContactSubmitModel.objects.create(first_name=form['first_name'],
                                              last_name=form['last_name'],
                                              email=form['email'],
                                              mobile=form['mobile'],
                                              message=form['message'])

            subject = 'welcome to Healfit'
            message_customer = 'Hi Wellcome to healfit'
            message_provider = f'full name: {form["first_name"]} {form["last_name"]} \n' \
                               f'emai: {form["email"]} \n' \
                               f'mobile: {form["mobile"]} \n' \
                               f'Message: {form["message"]}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [form['email']]

            send_mail(subject, message_customer, email_from, recipient_list)
            send_mail(subject, message_provider, email_from, ['no-reply@healfit.ae'])

            return Response(data={'message': 'successfully submitted'})
        else:
            return Response(data=ser_submit.errors)
