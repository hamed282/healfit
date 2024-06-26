from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('category_list/', views.ProductCategoryView.as_view(), name='product_list'),
    path('popular_product/', views.PopularProductView.as_view(), name='popular_product'),
    path('', views.ProductView.as_view(), name='product'),
    path('colorimage/', views.ProductColorImageView.as_view(), name='color_image'),
    path('variant/', views.ProductVariantShopView.as_view(), name='product_variant'),
    path('color_size', views.ColorSizeProductView.as_view(), name='color_size'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('list/', views.ProductListView.as_view(), name='product_list'),
    path('search_product/', views.SearchProductView.as_view({'get': 'list'}), name='search_product'),
    path('sizeofcolor/', views.SizeOfColorView.as_view(), name='size_of_color'),
    # path('<slug:slug>/', views.SnippetDetail.as_view(), name='snippet_detail'),
]
