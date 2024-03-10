from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MiddleBannerSliderModel, HomeSettingModel, ContactModel, ProductSettingModel, CartSettingModel,\
    BannerHomeModel, ContactSubmitModel
from .serializers import ContactSerializer, HomeSettingSerializer, MiddleBannerSliderSerializer,\
    ProductSettingSerializer, CartSettingSerializer, BannerHomeSerializer


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
        1. full_name
        2. email
        3. mobile
        4. message
        """
        form = request.data
        ContactSubmitModel.objects.create(full_name=form['full_name'],
                                          email=form['email'],
                                          mobile=form['mobile'],
                                          message=form['message'])
        return Response(data={'message': 'Done'})
