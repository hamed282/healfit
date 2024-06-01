from django.urls import path
from . import views


app_name = 'admin_panel'
urlpatterns = [
    path('product/', views.ProductView.as_view(), name='product'),
]
