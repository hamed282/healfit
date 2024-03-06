from django.db import models
from accounts.models import User
from product.models import ProductModel


class OrderModel(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_order')
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
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='order_product')
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    # class Meta:
    #     verbose_name = ''
    #     verbose_name_plural = ''

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
