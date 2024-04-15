import requests
import ssl
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
from requests.packages.urllib3.util import ssl_
from datetime import datetime
import sqlite3
import json
SITE = "www.avito.ru"


def get_json():


    cookies = {
        'gMltIuegZN2COuSe': 'EOFGWsm50bhh17prLqaIgdir1V0kgrvN',
        'u': '2xwj374i.1cyqcjt.nhxz3z4o9ug0',
        'buyer_laas_location': '637640',
        'luri': 'moskva',
        'buyer_location_id': '637640',
        '_gcl_au': '1.1.1620716757.1685364500',
        'tmr_lvid': '57db2f77905750a09c0665d50eaeb420',
        'tmr_lvidTS': '1685364500366',
        '_ga': 'GA1.1.1135022259.1685364500',
        '_ym_uid': '1685364501221625924',
        '_ym_d': '1685364501',
        '_ym_isad': '1',
        'uxs_uid': '179c8b90-fe1f-11ed-bf86-b303d6bc080a',
        'f': '5.32e32548b6f3e9784b5abdd419952845a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e94f9572e6986d0c624f9572e6986d0c624f9572e6986d0c62ba029cd346349f36c1e8912fd5a48d02c1e8912fd5a48d0246b8ae4e81acb9fa143114829cf33ca746b8ae4e81acb9fa46b8ae4e81acb9fae992ad2cc54b8aa8fbcd99d4b9f4cbdabcc8809df8ce07f640e3fb81381f359178ba5f931b08c66a59b49948619279110df103df0c26013a2ebf3cb6fd35a0ac91e52da22a560f550df103df0c26013a7b0d53c7afc06d0bba0ac8037e2b74f92da10fb74cac1eab71e7cb57bbcb8e0f71e7cb57bbcb8e0f71e7cb57bbcb8e0f0df103df0c26013a037e1fbb3ea05095de87ad3b397f946b4c41e97fe93686adecc9ea1e406218ca9538c5b98199aa035d3d12014bda85a47948e14b1edd0d45cc563a41f69613f929aa4cecca288d6b3c29848cab14088f8edb85158dee9a660df103df0c26013a0df103df0c26013aafbc9dcfc006bed91133b19e9465a10c0b7d7e24145d58a33de19da9ed218fe23de19da9ed218fe2d6fdecb021a45a31b3d22f8710f7c4ed78a492ecab7d2b7f',
        'ft': '"G6WKjONuIb5qn6WSAWltiiYjU90kMG51T+YJCIPPevJuLcyIgRNPQSJjwxNTTUH4wHjOGkP7GNLJyg2C2qDpNgbiFOafnL3C6V3aokJTK5lbzJSdI2TBR2ZvN4+EDEvsOn1omrznswsEi+yj7E6Yxp32WbvMpHQ/sGOaGXAQE8v7SlneMVmuKseMumCVxdgW"',
        'v': '1685367106',
        '_ym_visorc': 'b',
        'sx': 'H4sIAAAAAAAC%2F1TOyXGEMBAAwFz05qFrRjNko4v1gmwKxKXdIne%2F7LIT6Oq30NGiIpCgJejgsvU%2BkKIgswkqGhL9WxyiF3p%2B8Lyf%2B9dHnlSlqz71yHMafZlO5Ul0IoteIYEFA1bfnUBEjMnhwMiAFjm7kA0nBzJGl%2FhHrq9l8c86H423RnUfq60mX0NpYS1r%2BytLYro7kXUEHdkOirTLkoZkwdiAySWfYv49y0WdTZeVNzTT4%2FOo26thucrezIYc%2F58V3Pd3AAAA%2F%2F%2BbFixEDwEAAA%3D%3D',
        'redirectMav': '1',
        '_mlocation': '621540',
        '_mlocation_mode': 'default',
        '_inlines_order': 'params[504].owner.categoryNodes.locationGroup',
        'dfp_group': '52',
        '_ga_M29JC28873': 'GS1.1.1685367109.2.1.1685368380.56.0.0',
        'tmr_detect': '0%7C1685368382404',
    }

    headers = {
        'authority': 'm.avito.ru',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json;charset=utf-8',
        # 'cookie': 'gMltIuegZN2COuSe=EOFGWsm50bhh17prLqaIgdir1V0kgrvN; u=2xwj374i.1cyqcjt.nhxz3z4o9ug0; buyer_laas_location=637640; luri=moskva; buyer_location_id=637640; _gcl_au=1.1.1620716757.1685364500; tmr_lvid=57db2f77905750a09c0665d50eaeb420; tmr_lvidTS=1685364500366; _ga=GA1.1.1135022259.1685364500; _ym_uid=1685364501221625924; _ym_d=1685364501; _ym_isad=1; uxs_uid=179c8b90-fe1f-11ed-bf86-b303d6bc080a; f=5.32e32548b6f3e9784b5abdd419952845a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e94f9572e6986d0c624f9572e6986d0c624f9572e6986d0c62ba029cd346349f36c1e8912fd5a48d02c1e8912fd5a48d0246b8ae4e81acb9fa143114829cf33ca746b8ae4e81acb9fa46b8ae4e81acb9fae992ad2cc54b8aa8fbcd99d4b9f4cbdabcc8809df8ce07f640e3fb81381f359178ba5f931b08c66a59b49948619279110df103df0c26013a2ebf3cb6fd35a0ac91e52da22a560f550df103df0c26013a7b0d53c7afc06d0bba0ac8037e2b74f92da10fb74cac1eab71e7cb57bbcb8e0f71e7cb57bbcb8e0f71e7cb57bbcb8e0f0df103df0c26013a037e1fbb3ea05095de87ad3b397f946b4c41e97fe93686adecc9ea1e406218ca9538c5b98199aa035d3d12014bda85a47948e14b1edd0d45cc563a41f69613f929aa4cecca288d6b3c29848cab14088f8edb85158dee9a660df103df0c26013a0df103df0c26013aafbc9dcfc006bed91133b19e9465a10c0b7d7e24145d58a33de19da9ed218fe23de19da9ed218fe2d6fdecb021a45a31b3d22f8710f7c4ed78a492ecab7d2b7f; ft="G6WKjONuIb5qn6WSAWltiiYjU90kMG51T+YJCIPPevJuLcyIgRNPQSJjwxNTTUH4wHjOGkP7GNLJyg2C2qDpNgbiFOafnL3C6V3aokJTK5lbzJSdI2TBR2ZvN4+EDEvsOn1omrznswsEi+yj7E6Yxp32WbvMpHQ/sGOaGXAQE8v7SlneMVmuKseMumCVxdgW"; v=1685367106; _ym_visorc=b; sx=H4sIAAAAAAAC%2F1TOyXGEMBAAwFz05qFrRjNko4v1gmwKxKXdIne%2F7LIT6Oq30NGiIpCgJejgsvU%2BkKIgswkqGhL9WxyiF3p%2B8Lyf%2B9dHnlSlqz71yHMafZlO5Ul0IoteIYEFA1bfnUBEjMnhwMiAFjm7kA0nBzJGl%2FhHrq9l8c86H423RnUfq60mX0NpYS1r%2BytLYro7kXUEHdkOirTLkoZkwdiAySWfYv49y0WdTZeVNzTT4%2FOo26thucrezIYc%2F58V3Pd3AAAA%2F%2F%2BbFixEDwEAAA%3D%3D; redirectMav=1; _mlocation=621540; _mlocation_mode=default; _inlines_order=params[504].owner.categoryNodes.locationGroup; dfp_group=52; _ga_M29JC28873=GS1.1.1685367109.2.1.1685368380.56.0.0; tmr_detect=0%7C1685368382404',
        'referer': 'https://m.avito.ru/items/search?locationId=637640&localPriority=0&footWalkingMetro=0&categoryId=24&params[201]=1060&params[504]=5256&owner=private&sort=date&presentationType=serp',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'x-laas-timezone': 'Europe/Moscow',
    }


    CIPHERS = """ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:AES256-SHA"""

    class TlsAdapter(HTTPAdapter):

        def __init__(self, ssl_options=0, **kwargs):
            self.ssl_options = ssl_options
            super(TlsAdapter, self).__init__(**kwargs)

        def init_poolmanager(self, *pool_args, **pool_kwargs):
            ctx = ssl_.create_urllib3_context(
                ciphers=CIPHERS, cert_reqs=ssl.CERT_REQUIRED, options=self.ssl_options)
            self.poolmanager = PoolManager(
                *pool_args, ssl_context=ctx, **pool_kwargs)

    session = requests.session()
    adapter = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
    session.mount("https://", adapter)

    try:
        response = session.request('GET',
                                   'https://m.avito.ru/api/11/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&locationId=637640&localPriority=0&footWalkingMetro=0&categoryId=24&params[201]=1060&params[504]=5256&owner=private&sort=date&page=1&lastStamp=1685368320&display=list&limit=25&presentationType=serp',
                                   cookies=cookies,
                                   headers=headers,
        )
        data = response.json()
        with open('data.json', 'w') as file:
            json.dump(data, file)
    except Exception as exception:
        print(exception)
    
    return data


def get_offer(item):
    offer = {}
    offer['offer_id'] = item["value"]["id"]
    price = int(''.join(item["value"]["price"].replace(' ₽ в месяц', '').split()))
    offer['price'] = price
    offer['title'] = item['value']['title']
    elements = item["value"]["title"].split(', ')
    area = elements[1].replace("\xa0", "").replace("м²", '')
    if ',' in area:
        offer['area'] = int(area[:-2])
    else:
        offer['area'] = int(area)
    if "студия" in elements[0]:
        offer["rooms"] = 0
    else:
        offer["rooms"] = int(elements[0][0])
    offer['address'] = item['value']['address']
    #if item["value"].get("geoReferences"):
    undergrounds = []
    for undeground in item["value"]["geoReferences"]:
            undergrounds.append(undeground['content'])
    offer['undergrounds'] = ", ".join(undergrounds)
    #else:
        #offer['undergrounds'] = ''
    offer['url'] = SITE + item['value']['uri_mweb']
    timestamp = datetime.fromtimestamp(item['value']['time'])
    timestamp = datetime.strftime(timestamp, '%Y-%m-%d %H:%M:%S')
    offer['offer_date'] = timestamp
    return offer


def get_offers(data):
    for item in data["result"]["items"]:
        if item['type'] == 'item':
            check_database(item)


def check_database(item):
    offer_id = item["value"]["id"]
    with sqlite3.Connection("./db/realty.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT offer_id FROM offers WHERE offer_id = (?)
        """, (offer_id, ))
        result = cursor.fetchone()
        if result is None:
            offer = get_offer(item)
            cursor.execute("""
                INSERT INTO offers
                VALUES (NULL, :title, :price, :url, :offer_id, :offer_date, :area, :rooms, :address, :undergrounds)
            """, offer)
            connection.commit()
            print(f"Объявление {offer_id} добавлено в базу данных")


def main():
    data = get_json()
    get_offers(data)


if __name__ == "__main__":
    while True:
        main()
        time.sleep(12)
