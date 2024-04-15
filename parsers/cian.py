import requests
import ssl
from datetime import datetime
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
from requests.packages.urllib3.util import ssl_
import sqlite3


def get_json():

    cookies = {
        '_CIAN_GK': '5a6239c4-7ca2-458b-a3a6-0b948b662883',
        'uxfb_usertype': 'searcher',
        'tmr_lvid': '4c0c2a2772444f09b48555524490aebe',
        'tmr_lvidTS': '1673709656209',
        '_ym_uid': '1673709656468332482',
        '_ym_d': '1673709656',
        'uxs_uid': '0ac60500-941f-11ed-9f5d-a3b1ccb80331',
        '_gpVisits': '{"isFirstVisitDomain":true,"todayD":"Sat%20Jan%2014%202023","idContainer":"10002511"}',
        'afUserId': '6522a4b8-7d5b-4658-896d-f191794ab1d3-p',
        'cookie_agreement_accepted': '1',
        'forever_region_id': '1',
        'forever_region_name': '%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0',
        '_gcl_au': '1.1.1285092126.1681753098',
        '_hjSessionUser_2021803': 'eyJpZCI6IjIxZmMwZGVmLTEyYWMtNWM5YS05ZmQ3LWViOGNjM2VhNTljMiIsImNyZWF0ZWQiOjE2ODI3OTY5MzAwODMsImV4aXN0aW5nIjpmYWxzZX0=',
        'anti_bot': '"2|1:0|10:1684085127|8:anti_bot|44:eyJyZW1vdGVfaXAiOiAiMTc2LjEyMC4yNDcuMjE5In0=|0581c8228334b45213dbd7556ab82b149b50cbc0940c9db7f36c8f93b8d2c2dc"',
        'session_region_id': '1',
        'login_mro_popup': '1',
        'sopr_utm': '%7B%22utm_source%22%3A+%22direct%22%2C+%22utm_medium%22%3A+%22None%22%7D',
        'sopr_session': '09310f16266c4f83',
        '_gid': 'GA1.2.997935314.1684085131',
        '_ym_isad': '1',
        '_ym_visorc': 'b',
        'AF_SYNC': '1684085131719',
        'session_main_town_region_id': '1',
        'number_banner_appearances': '2',
        'viewpageTimer': '262.97400000000005',
        '__cf_bm': '7a1vtxBcmyT.j5PEwx9I3uXfTThyRrg8dZsJYq7TWHg-1684085444-0-ASbON6RF+eElewup8nfMb/cN89QtdIoAvEa0DiWGMYdhqdlO7fBAafru7FcvpCwNpV72BMMYR1Nr3BawHKIr7wo=',
        '_ga': 'GA1.2.1625641289.1673709656',
        '_ga_3369S417EL': 'GS1.1.1684085128.5.1.1684085620.60.0.0',
        '_dc_gtm_UA-30374201-1': '1',
    }

    headers = {
        'authority': 'api.cian.ru',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': '_CIAN_GK=5a6239c4-7ca2-458b-a3a6-0b948b662883; uxfb_usertype=searcher; tmr_lvid=4c0c2a2772444f09b48555524490aebe; tmr_lvidTS=1673709656209; _ym_uid=1673709656468332482; _ym_d=1673709656; uxs_uid=0ac60500-941f-11ed-9f5d-a3b1ccb80331; _gpVisits={"isFirstVisitDomain":true,"todayD":"Sat%20Jan%2014%202023","idContainer":"10002511"}; afUserId=6522a4b8-7d5b-4658-896d-f191794ab1d3-p; cookie_agreement_accepted=1; forever_region_id=1; forever_region_name=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; _gcl_au=1.1.1285092126.1681753098; _hjSessionUser_2021803=eyJpZCI6IjIxZmMwZGVmLTEyYWMtNWM5YS05ZmQ3LWViOGNjM2VhNTljMiIsImNyZWF0ZWQiOjE2ODI3OTY5MzAwODMsImV4aXN0aW5nIjpmYWxzZX0=; anti_bot="2|1:0|10:1684085127|8:anti_bot|44:eyJyZW1vdGVfaXAiOiAiMTc2LjEyMC4yNDcuMjE5In0=|0581c8228334b45213dbd7556ab82b149b50cbc0940c9db7f36c8f93b8d2c2dc"; session_region_id=1; login_mro_popup=1; sopr_utm=%7B%22utm_source%22%3A+%22direct%22%2C+%22utm_medium%22%3A+%22None%22%7D; sopr_session=09310f16266c4f83; _gid=GA1.2.997935314.1684085131; _ym_isad=1; _ym_visorc=b; AF_SYNC=1684085131719; session_main_town_region_id=1; number_banner_appearances=2; viewpageTimer=262.97400000000005; __cf_bm=7a1vtxBcmyT.j5PEwx9I3uXfTThyRrg8dZsJYq7TWHg-1684085444-0-ASbON6RF+eElewup8nfMb/cN89QtdIoAvEa0DiWGMYdhqdlO7fBAafru7FcvpCwNpV72BMMYR1Nr3BawHKIr7wo=; _ga=GA1.2.1625641289.1673709656; _ga_3369S417EL=GS1.1.1684085128.5.1.1684085620.60.0.0; _dc_gtm_UA-30374201-1=1',
        'origin': 'https://www.cian.ru',
        'referer': 'https://www.cian.ru/',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    data = '{"jsonQuery":{"_type":"flatrent","sort":{"type":"term","value":"creation_date_desc"},"engine_version":{"type":"term","value":2},"region":{"type":"terms","value":[1]},"is_by_homeowner":{"type":"term","value":true},"for_day":{"type":"term","value":"!1"},"repair":{"type":"terms","value":[2,3,4]}}}'


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
        response = session.request(
            'POST',
            'https://api.cian.ru/search-offers/v2/search-offers-desktop/',
            cookies=cookies,
            headers=headers,
            data=data)
        data = response.json()

    except Exception as exception:
        print(exception)
    return data


def get_offer(item):
    offer = {}
    offer['offer_id'] = item['id']
    offer['price'] = item['bargainTerms']['priceRur']
    if item["roomsCount"] is None:
        title = f'Квартира-студия, {item["totalArea"]} м², {item["floorNumber"]}/{item["building"]["floorsCount"]} этаж'
        offer["rooms"] = 0
    else:
        title = f'{item["roomsCount"]}-комн.кв., {item["totalArea"]} м², {item["floorNumber"]}/{item["building"]["floorsCount"]} этаж'
        offer["rooms"] = item["roomsCount"]
    offer['title'] = title
    offer['address'] = item['geo']['userInput']
    undergrounds = []
    for underground in item['geo']['undergrounds']:
        undergrounds.append(underground['name'])
    offer['undergrounds'] = ", ".join(undergrounds)
    offer['url'] = item['fullUrl']
    timestamp = datetime.fromtimestamp(item['addedTimestamp'])
    offer['offer_date'] = timestamp
    area = item["totalArea"]
    offer['area'] = float(area)
    offer['floor'] = item['floorNumber']
    return offer


def get_offers(data):
    for item in data['data']['offersSerialized']:
        check_database(item)


def check_database(item):
    offer_id = item['id']
    with sqlite3.connect("./db/realty.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT offer_id FROM offers WHERE offer_id = (?)
        """, (offer_id,))
        result = cursor.fetchone()
        if result is None:
            offer = get_offer(item)
            cursor.execute("""
                INSERT INTO offers
                VALUES (NULL, :title, :price, :url, :offer_id, :offer_date, :area, :rooms, :address, :undergrounds, :floor)
            """, offer)
            connection.commit()
            print(f"Объявление {offer_id} добавлено в базу данных")


def main():
    data = get_json()
    get_offers(data)


if __name__ == '__main__':
    while True:
        main()
        time.sleep(20)