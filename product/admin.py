from django.contrib import admin
from .models import ProductCategoryModel, ProductModel, PopularProductModel, SizeProductModel, ProductVariantModel,\
    ColorProductModel, ProductSubCategoryModel, AddSubCategoryModel


class ProductCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]


class ProductSubCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]


class SubCategoryInline(admin.TabularInline):
    model = AddSubCategoryModel
    # raw_id_fields = ('product',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product']
    readonly_fields = ["slug"]
    inlines = (SubCategoryInline,)


class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'color', 'size', 'quantity', 'price', 'percent_discount']
    readonly_fields = ["slug"]


class SizeProductAdmin(admin.ModelAdmin):
    list_display = ['size', 'priority']


admin.site.register(ProductCategoryModel, ProductCategoryAdmin)
admin.site.register(ProductSubCategoryModel, ProductSubCategoryAdmin)
admin.site.register(PopularProductModel)
admin.site.register(ProductModel, ProductAdmin)
admin.site.register(SizeProductModel, SizeProductAdmin)
admin.site.register(ProductVariantModel, ProductVariantAdmin)
admin.site.register(ColorProductModel)
