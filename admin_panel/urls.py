from django.urls import path
from . import views


app_name = 'admin_panel'
urlpatterns = [
    path('product/', views.ProductView.as_view(), name='product'),
    path('category/', views.CategoryView.as_view(), name='category'),
    path('category/search/', views.CategorySearchView.as_view(), name='category_search'),
    path('category/<int:category_id>/', views.CategoryItemView.as_view(), name='category_item'),
    path('login/', views.LoginUserView.as_view(), name='login'),
]
