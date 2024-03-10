from django.db import models
from accounts.models import User
from product.models import ProductModel, ColorProductModel, SizeProductModel
from accounts.models import AddressModel


class OrderModel(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_order')
    address = models.ForeignKey(AddressModel, on_delete=models.CASCADE, related_name='address_order')
    sent = models.BooleanField(default=False)
    ref_id = models.CharField(max_length=200, blank=True, null=True)
    cart_id = models.CharField(max_length=64, blank=True, null=True)
    trace = models.CharField(max_length=200, blank=True, null=True)
    error_message = models.TextField(blank=True, null=True)
    error_note = models.TextField(blank=True, null=True)

    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('paid', '-updated')
        #     verbose_name = ''
        #     verbose_name_plural = ''

    def __str__(self):
        return f'{self.user} - {self.id}'

    def get_total_price(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItemModel(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_order_item')
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='order_product')
    # color = models.ForeignKey(ColorProductModel, on_delete=models.CASCADE, related_name='order_color')
    # size = models.ForeignKey(SizeProductModel, on_delete=models.CASCADE, related_name='order_size')
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    completed = models.BooleanField(default=False)

    # class Meta:
    #     verbose_name = ''
    #     verbose_name_plural = ''

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
