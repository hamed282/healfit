from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact/', views.SocialMediaView.as_view(), name='contact'),
    path('banner_slider/', views.MiddleBannerSliderView.as_view(), name='banner_slider'),
    path('banner_slider/', views.MiddleBannerSliderView.as_view(), name='banner_slider'),
    path('product_setting/', views.ProductSettingView.as_view(), name='product_setting'),
    path('cart_setting/', views.CartSettingView.as_view(), name='cart_setting'),
]
