from django.contrib import admin
from .models import ProductCategoryModel, ProductModel, PopularProductModel, SizeProductModel, ProductVariantModel,\
    ColorProductModel, ProductSubCategoryModel


class ProductCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]


class ProductSubCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product']
    readonly_fields = ["slug"]


class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'color', 'size', 'quantity', 'price', 'percent_discount']
    readonly_fields = ["slug"]


class SizeProductAdmin(admin.ModelAdmin):
    list_display = ['size', 'priority']


admin.site.register(ProductCategoryModel, ProductCategoryAdmin)
admin.site.register(PopularProductModel)
admin.site.register(ProductModel, ProductAdmin)
admin.site.register(SizeProductModel, SizeProductAdmin)
admin.site.register(ProductVariantModel, ProductVariantAdmin)
admin.site.register(ColorProductModel)
admin.site.register(ProductSubCategoryModel, ProductSubCategoryAdmin)
