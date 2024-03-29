from decimal import Decimal
from django.conf import settings
from .serializers import ProductCartSerializer, QuantityProductSerializer
from .models import ProductModel
from rest_framework.response import Response


class Cart:
    def __init__(self, request):
        """
        initialize the cart
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        self.session.modified = True

    def add(self, product, quantity=1, overide_quantity=False):
        """
        Add product to the cart or update its quantity
        """

        product_id = str(product["id"])
        if product_id not in self.cart:
            self.cart[product_id] = {
                "quantity": 0,
                "off_price": str(product["off_price"])
            }
        if overide_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity

        product = ProductModel.objects.get(id=int(product_id))
        product = product.product_color_size.all()
        product = product.get(id=2)
        ser_product = QuantityProductSerializer(instance=product)
        quantity_stock = ser_product.data['quantity']
        if int(self.cart[product_id]["quantity"]) > int(quantity_stock):
            return {'massage': 'out of stock'}
        else:
            self.save()
            return {'massage': 'cart updated'}

    def remove(self, product):
        """
        Remove a product from the cart
        """
        product_id = str(product["id"])

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Loop through cart items and fetch the products from the database
        """
        product_ids = self.cart.keys()
        products = ProductModel.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]["product"] = ProductCartSerializer(product).data
        for item in cart.values():
            item["off_price"] = Decimal(item["off_price"])
            item["total_price"] = item["off_price"] * item["quantity"]
            yield item

    def __len__(self):
        """
        Count all items in the cart
        """
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item["off_price"]) * item["quantity"] for item in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()
