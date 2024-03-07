from django.db import models
from django.utils.text import slugify


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
    image4 = models.ImageField(upload_to='images/product/')
    image5 = models.ImageField(upload_to='images/product/')
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

    # class Meta:
    #     verbose_name = ''
    #     verbose_name_plural = ''

    def __str__(self):
        return f'{self.size}'


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
