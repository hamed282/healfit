from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
import json
import requests
from rest_framework import status
from .models import OrderModel, OrderItemModel
from product.models import ProductModel
from user_panel.models import UserProductModel


class OrderPayView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        parameters:
        1. product_id
        2. quantity

        sample json:

        [
        {"product_id": "2", "quantity": "2"} , {"product_id": "2", "quantity": "1"}
        ]
        """
        forms = request.data
        if len(forms) > 0:

            order = OrderModel.objects.create(user=request.user)

            for form in forms:
                product = ProductModel.objects.get(id=form['product_id'])
                quantity = form['quantity']
                price = product.get_off_price()
                OrderItemModel.objects.create(order=order, product=product, price=price, quantity=quantity)

            ############################################
            amount = order.get_total_price()
            description = f'buy'
            currency = "AED"
            test = "1"
            cart_id = "1234"

            payload = {
                "method": "create",
                "store": 1234,
                "authkey": "mykey1234",
                "framed": 0,
                "order": {
                    "cartid": cart_id,
                    "test": test,
                    "amount": amount,
                    "currency": currency,
                    "description": description,
                },
                "return": {
                    "authorised": "https://www.mysite.com/authorised",
                    "declined": "https://www.mysite.com/declined",
                    "cancelled": "https://www.mysite.com/cancelled"
                }
            }

            headers = {'Content-Type': 'application/json', 'accept': 'application/json'}
            response = requests.post(settings.TELR_API_REQUEST, json=payload, headers=headers, timeout=10)

            if response.status_code == 200:
                response = response.json()
                if 'order' in response:
                    url = response['url']
                    order.ref_id = response['ref']
                    order.cart_id = cart_id
                    order.save()
                    return Response({'redirect to : ': url}, status=200)
                else:
                    return Response({'Error code: ': str(response['error'])}, status=400)
            else:
                return Response({'details': str(response.json()['errors'])})


class OrderPayVerify(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.GET.get('Status') == 'OK':

            cart_id = request.GET.get('cartid')
            try:
                order = OrderModel.objects.get(cart_id=cart_id)
            except:
                return Response({'details': 'Cart ID not found'}, status=status.HTTP_401_UNAUTHORIZED)

            payload = {
                "method": "check",
                "store": 1234,
                "authkey": "mykey1234",
                "order": {"ref": order.ref_id}
            }
            headers = {
                "accept": "application/json",
                "Content-Type": "application/json"
            }
            response = requests.post(settings.TELR_API_VERIFY, json=payload, headers=headers)

            if response.status_code == 200:
                response = response.json()
                if 'order' in response:
                    order.trace = response['trace']

                    order.error_message = 'No Detail'
                    order.error_note = 'No Detail'
                    order.paid = True
                    order.save()
                    order_items = order.items.all()

                    for item in order_items:
                        product = item.product
                        price = product.get_off_price()
                        quantity = item.quantity

                        UserProductModel.objects.create(user=request.user, product=product, order=order,
                                                        quantity=quantity, price=price)

                    return Response({'details': 'Transaction success'}, status=status.HTTP_200_OK)

                else:
                    order.paid = False
                    order.trace = response['trace']
                    order.error_message = response['error']['message']
                    order.error_note = response['error']['note']

                    order.save()
                    return Response({'Error code: ': str(response['error'])}, status=400)

            else:
                return Response({'details': 'Transaction failed or canceled by user'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        else:
            return Response({'details': 'Transaction failed or canceled by user'}, status=status.HTTP_406_NOT_ACCEPTABLE)
