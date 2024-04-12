import requests
from .models import ProductModel, ProductVariantModel, ColorProductModel, SizeProductModel


def zoho():
    organization_id = '846612922'
    oauth = '1000.8e24be65274c0f0877213ace26fbec78.c25f3095cb1ba9bccc78d81893620853'
    per_page = '200'
    headers = {
        'Authorization': f"Zoho-oauthtoken {oauth}"}

    has_more_page = True
    page = 0
    i = 1
    while has_more_page:
        page += 1
        url_itemgroups = f'https://www.zohoapis.com/inventory/v1/itemgroups?organization_id={organization_id}&page={page}&per_page={per_page}'

        response_itemgroups = requests.get(url=url_itemgroups, headers=headers)
        response_itemgroups = response_itemgroups.json()

        for item in response_itemgroups['itemgroups']:
            try:
                product = item['group_name']
                group_id = item['group_id']
                print(i, product)

                product_exists = ProductModel.objects.filter(product=product)
                if product_exists.exists():
                    # product_obj = product_exists.get(product=product)
                    # product_obj.group_id = group_id
                    # product_obj.save()
                    pass

                else:
                    ProductModel.objects.create(product=product, group_id=group_id)

                i += 1
            except:
                continue
        has_more_page = response_itemgroups['page_context']['has_more_page']

    has_more_page = True
    page = 0
    i = 1
    while has_more_page:
        page += 1
        url_items = f'https://www.zohoapis.com/inventory/v1/items?organization_id={organization_id}&page={page}&per_page={per_page}'

        response_items = requests.get(url=url_items, headers=headers)
        response_items = response_items.json()

        for item in response_items['items']:
            try:
                product = item['group_name']
                product = ProductModel.objects.get(product=product)

                name = item['name']

                color = item['attribute_option_name1'].lower()
                color = ColorProductModel.objects.get(color=color)

                size = item['attribute_option_name2']
                size = SizeProductModel.objects.get(size=size)

                quantity = item['stock_on_hand']
                item_id = item['item_id']
                price = item['rate']
                print(i, name)
                product_variant = ProductVariantModel.objects.filter(name=name)
                if product_variant.exists():
                    product_obj = product_variant.get(name=name)
                    product_obj.quantity = quantity
                    product_obj.price = price
                    product_obj.save()

                else:
                    ProductVariantModel.objects.create(product=product,
                                                       name=name,
                                                       item_id=item_id,
                                                       color=color,
                                                       size=size,
                                                       price=price,
                                                       quantity=quantity)
                i += 1

            except:
                continue

        has_more_page = response_items['page_context']['has_more_page']

    # print(response['itemgroups'])


zoho()
