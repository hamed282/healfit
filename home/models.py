from django.db import models
from django.core.exceptions import ValidationError


class HomeSettingModel(models.Model):
    objects = None
    top_title = models.CharField(max_length=100, verbose_name='Section 1 Title', blank=True, null=True)
    top_description = models.TextField(verbose_name='Section 1 Description', blank=True, null=True)

    middle_title = models.CharField(max_length=100, verbose_name='Section 2 Title', blank=True, null=True)
    middle_description = models.TextField(verbose_name='Section 2 Description', blank=True, null=True)
    # middle_banner = models.ForeignKey(MiddleBannerSliderModel, on_delete=models.CASCADE)

    up_video = models.FileField(upload_to='videos/home', verbose_name='Section 3 Video', blank=True, null=True)
    up_video_title = models.CharField(max_length=100, verbose_name='Section 3 Title', blank=True, null=True)
    up_video_description = models.TextField(verbose_name='Section 3 Description', blank=True, null=True)

    button_banner = models.ImageField(upload_to='images/home/', verbose_name='Section 4 Image', blank=True, null=True)

    middle_video = models.FileField(upload_to='videos/home', verbose_name='Section 5 Video', blank=True, null=True)
    # middle_video_title = models.CharField(max_length=100, verbose_name='Section 5 Title', blank=True, null=True)
    middle_video_description = models.TextField(verbose_name='Section 5 Description', blank=True, null=True)

    banner = models.ImageField(upload_to='images/home/', verbose_name='Section 6 Image', blank=True, null=True)

    button_video = models.FileField(upload_to='videos/home', verbose_name='Section 7 Video', blank=True, null=True)
    button_video_title = models.CharField(max_length=100, verbose_name='Section 7 Title', blank=True, null=True)
    button_video_description = models.TextField(verbose_name='Section 7 Description', blank=True, null=True)

    footer_image = models.ImageField(upload_to='images/home/footer', verbose_name='Section 8 Image', blank=True, null=True)

    # class Meta:
    #     verbose_name = ''
    #     verbose_name_plural = ''

    def __str__(self):
        return f'Settings'

    def clean(self):
        if not self.pk and HomeSettingModel.objects.exists():
            # This below line will render error by breaking page, you will see
            raise ValidationError(
                "There can be only one Settings you can not add another"
            )


class ContactModel(models.Model):
    number = models.CharField(max_length=32, blank=True, null=True)
    # address = models.TextField(max_length=200, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    setting = models.ForeignKey(HomeSettingModel, on_delete=models.CASCADE, blank=True, null=True)

    # class Meta:
    #     verbose_name = 'Number-Header'
    #     verbose_name_plural = 'Number-Header'
    #     app_label = 'product'

    def __str__(self):
        return f'{self.number}'


class MiddleBannerSliderModel(models.Model):
    # title = models.CharField(max_length=100, blank=True, null=True)
    banner = models.ImageField(upload_to='images/home/', blank=True, null=True)
    setting = models.ForeignKey(HomeSettingModel, on_delete=models.CASCADE, blank=True, null=True)

    # class Meta:
    #     verbose_name = ''
    #     verbose_name_plural = ''

    def __str__(self):
        return f'middle banner'


class BannerHomeModel(models.Model):
    image = models.ImageField(upload_to='images/home/banner', blank=True, null=True)
    setting = models.ForeignKey(HomeSettingModel, on_delete=models.CASCADE, blank=True, null=True)

    # class Meta:
    #     verbose_name = ''
    #     verbose_name_plural = ''

    def __str__(self):
        return f'{self.setting}'


class ProductSettingModel(models.Model):
    objects = None
    size_chart = models.ImageField(upload_to='images/product/setting', blank=True, null=True)
    setting = models.ForeignKey(HomeSettingModel, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Size Chart - Shop Page'
        verbose_name_plural = 'Size Chart - Shop Page'

    def clean(self):
        if not self.pk and ProductSettingModel.objects.exists():
            # This below line will render error by breaking page, you will see
            raise ValidationError(
                "There can be only one Settings you can not add another"
            )


class CartSettingModel(models.Model):
    banner = models.ImageField(upload_to='images/cart/setting', blank=True, null=True)
    setting = models.ForeignKey(HomeSettingModel, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Banner-Cart page'
        verbose_name_plural = 'Banner-Cart page'

    def clean(self):
        if not self.pk and ProductSettingModel.objects.exists():
            # This below line will render error by breaking page, you will see
            raise ValidationError(
                "There can be only one Settings you can not add another"
            )
