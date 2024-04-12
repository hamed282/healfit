from django.contrib import admin
from .models import UserProductModel
from order.models import OrderItemModel


class OrderItemInline(admin.StackedInline):
    model = OrderItemModel
    extra = 1


# class UserProductAdmin(admin.ModelAdmin):
#     list_display = ['user']
    # inlines = (OrderItemInline,)


admin.site.register(UserProductModel)
