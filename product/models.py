from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models import Max


class ProductCategoryModel(models.Model):
    category = models.CharField(max_length=50)
    category_title = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    image = models.FileField(upload_to='images/category/')

    # class Meta:
    #     verbose_name = ''
    #     verbose_name_plural = ''

    def save(self, **kwargs):
        self.slug = slugify(self.category)
        super(ProductCategoryModel, self).save(**kwargs)

    def __str__(self):
        return f'{self.slug}'


class ProductModel(models.Model):
    objects = None
    category = models.ForeignKey(ProductCategoryModel, on_delete=models.CASCADE, related_name='category_product')
    product = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='images/product/')
    image2 = models.ImageField(upload_to='images/product/')
    image3 = models.ImageField(upload_to='images/product/')
    image4 = models.ImageField(upload_to='images/product/', blank=True, null=True)
    image5 = models.ImageField(upload_to='images/product/', blank=True, null=True)
    price = models.IntegerField()
    percent_discount = models.IntegerField(null=True, blank=True)
    product_code = models.CharField(max_length=100)
    is_available = models.BooleanField()
    slug = models.SlugField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # class Meta:
    #     verbose_name = ''
    #     verbose_name_plural = ''

    def save(self, **kwargs):
        self.slug = slugify(self.product)
        super(ProductModel, self).save(**kwargs)

    def __str__(self) -> str:
        return str(self.product)

    def get_off_price(self):
        price = self.price
        percent_discount = self.percent_discount
        if self.percent_discount is None:
            percent_discount = 0
        return int(price - price * percent_discount / 100)


class SizeProductModel(models.Model):
    objects = None
    size = models.CharField(max_length=120)
    priority = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     verbose_name = ''
    #     verbose_name_plural = ''

    def __str__(self):
        return f'{self.size}'


@receiver(pre_save, sender=SizeProductModel)
def increment_numbers_after_existing(sender, instance, **kwargs):
    if instance.pk:
        existing_instance = SizeProductModel.objects.get(pk=instance.pk)
        if not existing_instance.priority:
            last_number = SizeProductModel.objects.aggregate(max_number=Max('priority'))['max_number']
            existing_instance.priority = last_number
        current_priority = existing_instance.priority
        update_priority = instance.priority
        if current_priority > update_priority:
            SizeProductModel.objects.filter(priority__lt=current_priority, priority__gte=update_priority).update(
                priority=models.F('priority') + 1)
        if current_priority < update_priority:
            SizeProductModel.objects.filter(priority__gt=current_priority, priority__lte=update_priority).update(
                priority=models.F('priority') - 1)

    elif not instance.pk and not instance.priority:
        last_number = SizeProductModel.objects.aggregate(max_number=Max('priority'))['max_number']
        if last_number:
            instance.priority = last_number + 1
        else:
            instance.priority = 1

    elif not instance.pk and instance.priority:
        if SizeProductModel.objects.filter(priority__lte=instance.priority).exists():
            SizeProductModel.objects.filter(priority__gte=instance.priority).update(
                priority=models.F('priority') + 1)


class ColorProductModel(models.Model):
    color = models.CharField(max_length=120)
    color_code = models.CharField(max_length=120)

    # class Meta:
    #     verbose_name = ''
    #     verbose_name_plural = ''

    def __str__(self):
        return f'{self.color}'


class ProductVariantModel(models.Model):
    objects = None
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='product_color_size')
    color = models.ForeignKey(ColorProductModel, on_delete=models.CASCADE, related_name='color_product')
    size = models.ForeignKey(SizeProductModel, on_delete=models.CASCADE, related_name='size_product')
    quantity = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product', 'color', 'size'],
                name='unique_prod_color_size_combo'
            )
        ]
        #     verbose_name = ''
        #     verbose_name_plural = ''


class PopularProductModel(models.Model):
    objects = None
    popular = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='popular_product')

    # class Meta:
    #     verbose_name = ''
    #     verbose_name_plural = ''

    def __str__(self):
        return f'{self.popular}'
