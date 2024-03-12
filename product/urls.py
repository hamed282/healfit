from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('category_list/', views.ProductCategoryView.as_view(), name='product_list'),
    path('popular_product/', views.PopularProductView.as_view(), name='popular_product'),
    path('', views.ProductView.as_view(), name='product'),
    path('color_size', views.ColorSizeProductView.as_view(), name='color_size'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('list/', views.ProductListView.as_view(), name='product_list')
]
