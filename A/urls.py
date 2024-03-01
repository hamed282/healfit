from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home_slider/', views.HomeSliderView.as_view(), name='home_slider'),

    path('api-auth/', include('rest_framework.urls')),
    path('api/accounts/', include('accounts.urls', namespace='accounts')),
    path('api/cart/', include('cart.urls', namespace='cart')),
    path('api/home/', include('home.urls', namespace='home')),
    path('api/product/', include('product.urls', namespace='product')),
    path('api/order/', include('order.urls', namespace='order')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
