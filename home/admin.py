from django.contrib import admin
from .models import HomeSettingModel, MiddleBannerSliderModel, ContactModel, CartSettingModel, ProductSettingModel,\
    BannerHomeModel, ContactSubmitModel


class BannerHomeInline(admin.StackedInline):
    model = BannerHomeModel
    extra = 1
    # raw_id_fields = ('product',)


class BannerSliderInline(admin.StackedInline):
    model = MiddleBannerSliderModel
    extra = 1
    # raw_id_fields = ('product',)


class ContactInline(admin.StackedInline):
    extra = 1
    model = ContactModel
    # raw_id_fields = ('product',)


class SizeChartInline(admin.StackedInline):
    model = ProductSettingModel
    extra = 1
    # raw_id_fields = ('product',)


class CartSettingInline(admin.StackedInline):
    model = CartSettingModel
    extra = 1
    # raw_id_fields = ('product',)


@admin.register(HomeSettingModel)
class HomeSettingAdmin(admin.ModelAdmin):
    # list_display = ('id', 'user', 'updated', 'paid')
    # list_filter = ('paid',)
    fieldsets = (
        ('Section 1(Home Page)', {
            'fields': ('top_title', 'top_description')
        }),
        ('Section 2(Home Page)', {
            'fields': ('middle_title', 'middle_description')
        }),
        ('Section 3(Home Page)', {
            'fields': ('up_video', 'up_video_title', 'up_video_description')
        }),
        ('Section 4(Home Page)', {
            'fields': ('button_banner',)
        }),
        ('Section 5(Home Page)', {
            'fields': ('middle_video', 'middle_video_description')
        }),
        ('Section 6(Home Page)', {
            'fields': ('banner',)
        }),
        ('Section 7(Home Page)', {
            'fields': ('button_video', 'button_video_title', 'button_video_description')
        }),
        ('Footer', {
            'fields': ('footer_image',)
        }),
    )

    def staff(self, obj):
        return obj.is_staff

    staff.short_description = "Staff"

    inlines = (BannerHomeInline, BannerSliderInline, ContactInline, SizeChartInline, CartSettingInline)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'mobile']


admin.site.register(ContactSubmitModel, ContactAdmin)
