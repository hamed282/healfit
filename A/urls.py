from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.contrib.sitemaps.views import sitemap
from product.sitemaps import ProductWomenViewSitemap, ProductMenViewSitemap, SnippetSitemap


sitemaps = {
    'product_women': ProductWomenViewSitemap,
    'product_men': ProductMenViewSitemap,
    'product_snippet': SnippetSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls', namespace='accounts')),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/home/', include('home.urls', namespace='home')),
    path('api/product/', include('product.urls', namespace='product')),
    path('api/order/', include('order.urls', namespace='order')),
    path('api/admin/', include('admin_panel.urls', namespace='admin_panel')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
