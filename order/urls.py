from django.urls import path
from . import views


app_name = 'order'
urlpatterns = [
    path('pay/', views.OrderPayView.as_view(), name='order')
]

