from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
import requests
from .models import OrderModel, OrderItemModel
from product.models import ProductModel, ColorProductModel, SizeProductModel, ProductVariantModel
from user_panel.models import UserProductModel
from accounts.models import AddressModel
from django.shortcuts import get_object_or_404
from .serializers import OrderUserSerializer
# from utils import zoho_item_quantity_update


class OrderPayView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        parameters:
        1. product_id
        2. quantity
        3. address_id

        sample json:
        {
        "product": [
                    {"product_id": "1", "quantity": "2", "color": "black", "size": "X"} ,
                     {"product_id": "1", "quantity": "2", "color": "black", "size": "X"}
                   ],
        "address_id": "6"
        }
        """
        forms = request.data['product']
        data = request.data

        if len(forms) > 0:
            address = get_object_or_404(AddressModel, id=data['address_id'])
            order = OrderModel.objects.create(user=request.user, address=address)

            for form in forms:
                color = get_object_or_404(ColorProductModel, color=form['color'])
                size = get_object_or_404(SizeProductModel, size=form['size'])

                product_group = ProductModel.objects.get(id=form['product_id'])
                product = ProductVariantModel.objects.get(product=product_group, color=color, size=size)
                quantity = form['quantity']

                price = product.get_off_price()
                item_id = product.item_id
                OrderItemModel.objects.create(order=order,
                                              user=request.user,
                                              product=product,
                                              price=price,
                                              quantity=quantity,
                                              color=color,
                                              size=size,
                                              item_id=item_id)
            ############################################
            amount = str(order.get_total_price())
            description = f'buy'
            cart_id = str(order.id)
            payload = {
                "method": "create",
                "store": settings.SOTRE_ID,
                "authkey": settings.AUTHKEY,
                "framed": settings.FRAMED,
                "order": {
                    "cartid": cart_id,
                    "test": settings.TEST,
                    "amount": amount,
                    "currency": settings.CURRENCY,
                    "description": description,
                },
                "return": {
                    "authorised": settings.AUTHORIZED_URL,
                    "declined": settings.DECLINED_URL,
                    "cancelled": settings.CANCELLED_URL,
                }
            }

            headers = {'Content-Type': 'application/json', 'accept': 'application/json'}
            response = requests.post(settings.TELR_API_REQUEST, json=payload, headers=headers, timeout=10)
            if response.status_code == 200:
                response = response.json()

                if 'order' in response:
                    url = response['order']['url']
                    order.ref_id = response['order']['ref']
                    order.cart_id = cart_id
                    order.save()
                    return Response({'redirect to : ': url}, status=200)
                else:
                    return Response({'Error code: ': str(response['error'])}, status=400)
            else:
                return Response({'details': str(response.json()['errors'])})


# class OrderPayVerifyView(APIView):
#
#     def get(self, request):
#         if request.GET.get('Status') == 'OK':
#             print('-' * 100)
#             cart_id = request.GET.get('cartid')
#             print(cart_id)
#             try:
#                 order = OrderModel.objects.get(cart_id=cart_id)
#             except:
#                 return Response({'details': 'Cart ID not found'}, status=status.HTTP_401_UNAUTHORIZED)
#
#             payload = {
#                 "method": "check",
#                 "store": settings.SOTRE_ID,
#                 "authkey": settings.AUTHKEY,
#                 "order": {"ref": order.ref_id}
#             }
#             headers = {
#                 "accept": "application/json",
#                 "Content-Type": "application/json"
#             }
#             response = requests.post(settings.TELR_API_VERIFY, json=payload, headers=headers)
#
#             if response.status_code == 200:
#                 response = response.json()
#                 if 'order' in response:
#                     order.trace = response['trace']
#
#                     order.error_message = 'No Detail'
#                     order.error_note = 'No Detail'
#                     order.paid = True
#                     order.save()
#                     order_items = order.items.all()
#
#                     # quantity =
#
#                     for item in order_items:
#                         product = item.product
#                         price = product.get_off_price()
#                         quantity = item.quantity
#
#                         UserProductModel.objects.create(user=request.user, product=product, order=order,
#                                                         quantity=quantity, price=price)
#
#                     return Response({'details': 'Transaction success'}, status=status.HTTP_200_OK)
#
#                 else:
#                     order.paid = False
#                     order.trace = response['trace']
#                     order.error_message = response['error']['message']
#                     order.error_note = response['error']['note']
#
#                     order.save()
#                     return Response({'Error code: ': str(response['error'])}, status=400)
#
#             else:
#                 return Response({'details': 'Transaction failed or canceled by user'}, status=status.HTTP_406_NOT_ACCEPTABLE)
#
#         else:
#             return Response({'details': 'Transaction failed or canceled by user'}, status=status.HTTP_406_NOT_ACCEPTABLE)


class OrderPayAuthorisedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        try:
            order = OrderModel.objects.filter(user=user).first()
        except:
            # return HttpResponseRedirect(redirect_to='https://gogle.com')
            return Response(data={'message': 'invalid order'})

        payload = {
            "method": "check",
            "store": settings.SOTRE_ID,
            "authkey": settings.AUTHKEY,
            "order": {"ref": order.ref_id}
        }
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        ## to do: if quantity = 0 dont send request

        response = requests.post(settings.TELR_API_VERIFY, json=payload, headers=headers)
        response = response.json()

        if 'order' in response:
            order.trace = response['trace']

            order.error_message = 'No Detail'
            order.error_note = 'No Detail'
            order.paid = True
            order.save()
            order_items = order.items.all()

            for item in order_items:
                product_variant = item.product
                price = product_variant.get_off_price()
                quantity = item.quantity

                # try:
                #     stock_on_hand = zoho_item_quantity_update(item.item_id, quantity)
                #     # product_variant = ProductVariantModel.objects.get(product=product, color=item.color, size=item.size)
                #     product_variant.quantity = stock_on_hand
                #     product_variant.save()
                # except:
                #     # product_variant = ProductVariantModel.objects.get(product=product, color=item.color, size=item.size)
                #     product_variant.quantity = product_variant.quantity - quantity
                #     product_variant.save()

                # try:
                #     stock_on_hand = zoho_item_quantity_update(item.item_id, quantity)
                #     # product_variant = ProductVariantModel.objects.get(product=product, color=item.color, size=item.size)
                #     product_variant.quantity = stock_on_hand
                #     product_variant.save()
                # except:
                #     # product_variant = ProductVariantModel.objects.get(product=product, color=item.color, size=item.size)
                #     product_variant.quantity = product_variant.quantity - quantity
                #     product_variant.save()

                product_variant.quantity = product_variant.quantity - quantity
                product_variant.save()

                item.completed = True
                item.trace = response['trace']
                item.save()

                UserProductModel.objects.create(user=user, product=product_variant, order=order,
                                                quantity=quantity, price=price)

            # return HttpResponseRedirect(redirect_to='https://gogle.com')
            return Response(data={'message': 'success', 'cart_id': order.cart_id, 'trace':response['trace']})

        else:
            order.paid = False
            order.trace = response['trace']
            order.error_message = response['error']['message']
            order.error_note = response['error']['note']

            order.save()
            # return HttpResponseRedirect(redirect_to='https://gogle.com')
            return Response(data={'message': 'failed'})


class OrderPayDeclinedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        # from accounts.models import User
        # user = User.objects.get(id=1)

        try:
            order = OrderModel.objects.filter(user=user).first()
        except:
            return Response(data={'message': 'invalid order'})
        payload = {
            "method": "check",
            "store": settings.SOTRE_ID,
            "authkey": settings.AUTHKEY,
            "order": {"ref": order.ref_id}
        }
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        response = requests.post(settings.TELR_API_VERIFY, json=payload, headers=headers)
        response = response.json()

        order.paid = False
        order.trace = response['trace']
        order.error_message = 'Declined'
        order.save()

        return Response(data={'message': 'Declined'})


class OrderPayCancelledView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        # from accounts.models import User
        # user = User.objects.get(id=1)

        try:
            order = OrderModel.objects.filter(user=user).first()
        except:
            return Response(data={'message': 'invalid order'})
        payload = {
            "method": "check",
            "store": settings.SOTRE_ID,
            "authkey": settings.AUTHKEY,
            "order": {"ref": order.ref_id}
        }
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        response = requests.post(settings.TELR_API_VERIFY, json=payload, headers=headers)
        response = response.json()

        order.paid = False
        order.trace = response['trace']
        order.error_message = 'canceled'
        order.save()

        return Response(data={'message': 'Cancelled'})


class OrderHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        order_history = OrderItemModel.objects.filter(user=request.user, completed=True)
        ser_order_history = OrderUserSerializer(instance=order_history, many=True)
        return Response(data=ser_order_history.data)
