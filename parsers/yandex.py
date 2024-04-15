import requests
import ssl
import time
from datetime import datetime
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
from requests.packages.urllib3.util import ssl_
import sqlite3


def get_json():

    cookies = {
        'yandexuid': '2733884821667847059',
        'yandex_gid': '118759',
        'gdpr': '0',
        '_ym_uid': '1680038606117969825',
        '_ym_d': '1680038606',
        'suid': '58902b3a48424eeb347b5eddabcdb373.30645b323137ca56512281276250daad',
        'i': 'MsLzwYQWKT6m6sEG+581I6iLxWwVIUpS9cxHkQ9dXxEb0bFXRbNfMcsttz6u0qOPIOrfd/+7rusWh2fWWxxP3N/4ze0=',
        'font_loaded': 'YSv1',
        'tmr_lvid': '666de841c91f74856b53c3ea8b539392',
        'tmr_lvidTS': '1680038680691',
        'link_to_global_tooltip_shown': 'YES',
        'KIykI': '1',
        'is_gdpr': '0',
        'is_gdpr_b': 'CIHuMRDCsQEoAg==',
        '_yasc': '6U3IufW6lLv/3jC7hS+IZeRVNyDNrIL9O+QnqMo9fVg9bwSqVkMgmTxbmxyDwQ==',
        'yandex_csyr': '1681400635',
        'splash_banner_closed': '1',
        'L': 'AhIBVwZwe1xPQH1Wc2kAWWR8BFMJbmFyPRQkLVZKBVcjU31XAwU=.1681496505.15312.334289.744c5df9dfc5a05e449bea3ef94317fc',
        '_ym_isad': '1',
        '_ym_visorc': 'b',
        'spravka': 'dD0xNjgxODI4MDgyO2k9MTc2LjEyMC4yMzAuMTYxO0Q9RTFBMDAyQjFFRTgyRThGODgyNzc3ODVBOUQ0NTFBQ0FFODBBOTkwQTRCNUQ0RjAyOEI2NzU0MTJENzcwMUZDMEMxQUFBMTU5MTJCMUNCOEQ5MDE1NTI5QTdFQzg3RUI3MUQ0NjlEO3U9MTY4MTgyODA4Mjk5MDk4OTc5MjtoPWU4NTQ2OGU0YmZiY2VjNTJlZWYxNzBiNmMxMzVjMDM5',
        '_csrf_token': 'a7af3011496cae6c3d0dcb07eb05783b4aca1b13668410eb',
        '_yasc': 'ZN/s4CPeZPn99w6eJbIWj8tllf4czEy11BhT+ijPoyP6Elyrl9C+Zzz4hW/RFQ==',
        'sso_status': 'sso.passport.yandex.ru:synchronized',
        'from': 'other',
        'yandex_login': '',
        'yp': '1674386018.szm.1_25:1536x864:1536x722#1676812592.ygu.1#1678711928.yu.4820659071678621300#1995398644.multib.1',
        'Session_id': 'noauth:1681828360',
        'ys': 'udn.cDpFbGk%3D#c_chck.3781030373',
        'mda2_beacon': '1681828360194',
        'prev_uaas_data': '2733884821667847059%23743188%23733227%23729450%23741613%23733672%23733543%23742471%23714302%23751417%23213160%23361531%23610827%23728649',
        'prev_uaas_expcrypted': 'zZeCO_ExIHsEel6OXR_t4pla6ICf8dBgqmyLud9sLa26hl50FyOpSTCqOR9SeG_lQmdY5JsJMUKeDj4roCIycQSEpayaOs7LmvVETWFCSKVfCnhMk18A84BP2KNFMqr_R9IunhL8anqWaT4L6TItjIIsKVCNzb2IiNo5tombS44BjkgBA2p4O6xfutYXAueshM-ruM8mlk4c3AB68ajIlA%2C%2C',
        'tmr_detect': '1%7C1681828419538',
        'rgid': '587795',
        'from_lifetime': '1681828466096',
    }

    headers = {
        'authority': 'realty.ya.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'client-view-type': 'touch-phone',
        # 'cookie': 'yandexuid=2733884821667847059; yandex_gid=118759; gdpr=0; _ym_uid=1680038606117969825; _ym_d=1680038606; suid=58902b3a48424eeb347b5eddabcdb373.30645b323137ca56512281276250daad; i=MsLzwYQWKT6m6sEG+581I6iLxWwVIUpS9cxHkQ9dXxEb0bFXRbNfMcsttz6u0qOPIOrfd/+7rusWh2fWWxxP3N/4ze0=; font_loaded=YSv1; tmr_lvid=666de841c91f74856b53c3ea8b539392; tmr_lvidTS=1680038680691; link_to_global_tooltip_shown=YES; KIykI=1; is_gdpr=0; is_gdpr_b=CIHuMRDCsQEoAg==; _yasc=6U3IufW6lLv/3jC7hS+IZeRVNyDNrIL9O+QnqMo9fVg9bwSqVkMgmTxbmxyDwQ==; yandex_csyr=1681400635; splash_banner_closed=1; L=AhIBVwZwe1xPQH1Wc2kAWWR8BFMJbmFyPRQkLVZKBVcjU31XAwU=.1681496505.15312.334289.744c5df9dfc5a05e449bea3ef94317fc; _ym_isad=1; _ym_visorc=b; spravka=dD0xNjgxODI4MDgyO2k9MTc2LjEyMC4yMzAuMTYxO0Q9RTFBMDAyQjFFRTgyRThGODgyNzc3ODVBOUQ0NTFBQ0FFODBBOTkwQTRCNUQ0RjAyOEI2NzU0MTJENzcwMUZDMEMxQUFBMTU5MTJCMUNCOEQ5MDE1NTI5QTdFQzg3RUI3MUQ0NjlEO3U9MTY4MTgyODA4Mjk5MDk4OTc5MjtoPWU4NTQ2OGU0YmZiY2VjNTJlZWYxNzBiNmMxMzVjMDM5; _csrf_token=a7af3011496cae6c3d0dcb07eb05783b4aca1b13668410eb; _yasc=ZN/s4CPeZPn99w6eJbIWj8tllf4czEy11BhT+ijPoyP6Elyrl9C+Zzz4hW/RFQ==; sso_status=sso.passport.yandex.ru:synchronized; from=other; yandex_login=; yp=1674386018.szm.1_25:1536x864:1536x722#1676812592.ygu.1#1678711928.yu.4820659071678621300#1995398644.multib.1; Session_id=noauth:1681828360; ys=udn.cDpFbGk%3D#c_chck.3781030373; mda2_beacon=1681828360194; prev_uaas_data=2733884821667847059%23743188%23733227%23729450%23741613%23733672%23733543%23742471%23714302%23751417%23213160%23361531%23610827%23728649; prev_uaas_expcrypted=zZeCO_ExIHsEel6OXR_t4pla6ICf8dBgqmyLud9sLa26hl50FyOpSTCqOR9SeG_lQmdY5JsJMUKeDj4roCIycQSEpayaOs7LmvVETWFCSKVfCnhMk18A84BP2KNFMqr_R9IunhL8anqWaT4L6TItjIIsKVCNzb2IiNo5tombS44BjkgBA2p4O6xfutYXAueshM-ruM8mlk4c3AB68ajIlA%2C%2C; tmr_detect=1%7C1681828419538; rgid=587795; from_lifetime=1681828466096',
        'referer': 'https://realty.ya.ru/moskva/snyat/kvartira/bez-posrednikov/?sort=DATE_DESC&pricingPeriod=PER_MONTH',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'x-metrika-client-id': '1680038606117969825',
        'x-requested-with': 'XMLHttpRequest',
        'x-retpath-y': 'https://realty.ya.ru/moskva/snyat/kvartira/bez-posrednikov/?sort=DATE_DESC&pricingPeriod=PER_MONTH',
    }

    params = {
        'sort': 'DATE_DESC',
        'pricingPeriod': 'PER_MONTH',
        'rgid': '587795',
        'type': 'RENT',
        'category': 'APARTMENT',
        'agents': 'NO',
        '_pageType': 'search',
        '_providers': [
            'search-results',
            'search-presets',
            'refinements',
            'breadcrumbs',
            'geo',
            'ads',
            'seo',
            'seo-texts',
            'cache-footer-links',
            'filters',
            'client-search-params',
            'search-results-query',
            'serp-snippets',
            'samolet-plus-serp-snippets',
            'reviews',
            'related-newbuildings',
            'ya-arenda-rent-pladge-snippets',
        ],
        'crc': 'y3261bdc1adeb7916778e78309348960a',
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
        response = session.request(
            'GET',
            'https://realty.ya.ru/gate/react-page/get/',
            params=params,
            cookies=cookies,
            headers=headers)
        data = response.json()
    except Exception as exception:
        print(exception)

    return data


def get_offer(item):
    offer = {}
    if item.get("roomsTotal"):
        title = f'{str(item["roomsTotal"])}-к. квартира, {str(item["area"]["value"])}м², {str(item["floorsOffered"][0])}/{str(item["floorsTotal"])}эт.'
        offer['title'] = title
        offer['rooms'] = item["roomsTotal"]
    else:
        title = f'{str(item["area"]["value"])}м², квартира-студия'
        offer['title'] = title
        offer['rooms'] = 0
    offer['url'] = item['shareUrl']
    offer["offer_id"] = int(item["offerId"])
    if item.get('updateDate'):
        offer_date = item['updateDate'].replace("T", " ").replace("Z", "")
    else:
        offer_date = item['creationDate'].replace("T", " ").replace("Z", "")
    offer['offer_date'] = offer_date
    offer['price'] = item['price']['value']
    offer['address'] = item['location']['address']
    undergrounds = []
    for underground in item['location']['metroList']:
        undergrounds.append(underground['name'])
    offer['undergrounds'] = ", ".join(undergrounds)
    offer['area'] = item["area"]["value"]
    offer['floor'] = item['floorsOffered'][0]
    return offer


def get_offers(data):
    for item in data['response']['searchResults']['entities']:
        check_database(item)
        

def check_database(item):
    offer_id = int(item["offerId"])
    with sqlite3.connect("./db/realty.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT offer_id FROM offers WHERE offer_id = (?)
        """, (offer_id, ))
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
