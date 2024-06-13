from django.urls import path
from . import views


app_name = 'admin_panel'
urlpatterns = [
    path('product/', views.ProductView.as_view(), name='product'),
    path('category/', views.CategoryView.as_view(), name='category'),
    # path('category/<int:id_category>/', views.CategoryView.as_view(), name='category_delete'),
]
