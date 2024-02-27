from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls', namespace='accounts')),
    path('api/cart/', include('cart.urls', namespace='cart')),
    path('api/home/', include('home.urls', namespace='home')),
    path('api/product/', include('product.urls', namespace='product')),
    path('api/order/', include('order.urls', namespace='order')),
]
