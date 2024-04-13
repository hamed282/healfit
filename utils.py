from django.conf import settings
import requests


def zoho_refresh_token():
    client_id = settings.CLIENT_ID
    client_secret = settings.CLIENT_SECRET
    grant_type = settings.GRANT_TYPE
    scope = settings.SCOPE_READING
    soid = settings.SIOD

    url_refresh_token = f'https://accounts.zoho.com/oauth/v2/token?client_id={client_id}&client_secret={client_secret}&grant_type={grant_type}&scope={scope}&soid={soid}'
    response_refresh_token = requests.post(url=url_refresh_token)
    response_refresh_token = response_refresh_token.json()
    response_refresh = response_refresh_token['access_token']

    return response_refresh


def zoho_refresh_token_update():
    client_id = settings.CLIENT_ID
    client_secret = settings.CLIENT_SECRET
    grant_type = settings.GRANT_TYPE
    scope = settings.SCOPE_UPDATE
    soid = settings.SIOD

    url_refresh_token = f'https://accounts.zoho.com/oauth/v2/token?client_id={client_id}&client_secret={client_secret}&grant_type={grant_type}&scope={scope}&soid={soid}'
    response_refresh_token = requests.post(url=url_refresh_token)
    response_refresh_token = response_refresh_token.json()
    response_refresh = response_refresh_token['access_token']

    return response_refresh


def zoho_item_quantity_update(item_id, quantity):
    organization_id = settings.ORGANIZATION_ID
    oauth = zoho_refresh_token()
    headers = {
        'Authorization': f"Zoho-oauthtoken {oauth}"}
    url_item = f'https://www.zohoapis.com/inventory/v1/itemdetails?item_ids={item_id}&organization_id={organization_id}'
    response_item = requests.get(url=url_item, headers=headers)
    response_item = response_item.json()
    stock_on_hand = response_item['items'][0]['stock_on_hand']

    organization_id = settings.ORGANIZATION_ID
    oauth = zoho_refresh_token_update()
    item_id = item_id
    url_item = f'https://www.zohoapis.com/inventory/v1/items/{item_id}?organization_id={organization_id}'

    headers = {
        'Authorization': f"Zoho-oauthtoken {oauth}",
        'content-type': "application/json"}
    update_stock = int(stock_on_hand) - quantity
    payload = {'stock_on_hand': f'{update_stock}'}

    response_item = requests.put(url=url_item, headers=headers, json=payload)
    response_item = response_item.json()
    # quantity = response_item['stock_on_hand']
    # print(quantity)
    return update_stock
