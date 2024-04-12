from django.db import models
from accounts.models import User
from product.models import ProductVariantModel
from order.models import OrderModel


class UserProductModel(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rel_user')
    product = models.ForeignKey(ProductVariantModel, on_delete=models.CASCADE, related_name='rel_product')
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='rel_order')
    price = models.CharField(max_length=20)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.order}'
