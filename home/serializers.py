from rest_framework import serializers
from .models import ContactModel, MiddleBannerSliderModel, HomeSettingModel, CartSettingModel, ProductSettingModel,\
    BannerHomeModel


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = '__all__'


class BannerHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerHomeModel
        fields = ['image']


class HomeSettingSerializer(serializers.ModelSerializer):
    banner_home = BannerHomeSerializer(read_only=True, many=True)

    class Meta:
        model = HomeSettingModel
        fields = '__all__'


class MiddleBannerSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiddleBannerSliderModel
        fields = '__all__'


class CartSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartSettingModel
        fields = '__all__'


class ProductSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSettingModel
        fields = '__all__'
