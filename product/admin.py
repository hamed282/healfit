from django.contrib import admin
from .models import (ProductCategoryModel, ProductModel, PopularProductModel, SizeProductModel, ProductVariantModel,
                     ColorProductModel, ProductSubCategoryModel, AddSubCategoryModel, AddCategoryModel,
                     ProductGenderModel, AddImageGalleryModel, ExtraGroupModel)
from django.utils.html import format_html


class ProductGenderAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]


class ProductCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]


class ProductSubCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]


class ProductImageGalleryAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))
    list_display = ['product', 'color', 'image_tag']


class CategoryInline(admin.TabularInline):
    model = AddCategoryModel
    # raw_id_fields = ('product',)
    extra = 1


class SubCategoryInline(admin.TabularInline):
    model = AddSubCategoryModel
    # raw_id_fields = ('product',)
    extra = 1


class ImageGalleryInline(admin.TabularInline):
    model = AddImageGalleryModel
    # raw_id_fields = ('product',)
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'priority']
    readonly_fields = ["slug"]
    inlines = (ImageGalleryInline, CategoryInline, SubCategoryInline)


class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'color', 'size', 'quantity', 'price', 'percent_discount']
    readonly_fields = ["slug"]


class SizeProductAdmin(admin.ModelAdmin):
    list_display = ['size', 'priority']


admin.site.register(ProductCategoryModel, ProductCategoryAdmin)
admin.site.register(ProductGenderModel, ProductGenderAdmin)
admin.site.register(ProductSubCategoryModel, ProductSubCategoryAdmin)
admin.site.register(AddImageGalleryModel, ProductImageGalleryAdmin)
admin.site.register(PopularProductModel)
admin.site.register(ProductModel, ProductAdmin)
admin.site.register(SizeProductModel, SizeProductAdmin)
admin.site.register(ProductVariantModel, ProductVariantAdmin)
admin.site.register(ColorProductModel)
admin.site.register(ExtraGroupModel)
