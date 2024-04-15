from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
#from fake_useragent import UserAgent
import sqlite3

month = {
    'января' : '01',
    'февраля' : '02',
    'марта': '03',
    'апреля': '04',
    'мая': '05',
    'июня': '06',
    'июля': '07',
    'августа': '08',
    'сентября': '09',
    'октября': '10',
    'ноября': '11',
    'декабря': '12'
}

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
#options
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={useragent}')
#options.add_argument('--proxy-server=176.53.143.37:8000')
#disable webdriver mode
options.add_argument('--disable-blink-features=AutomationControlled')
#headless mode
#options.headless = True

url = 'https://www.avito.ru/moskva/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?f=ASgBAQICAkSSA8gQ8AeQUgFA7MENNIbPOYTPOYLPOQ&s=104&user=1'
driver = webdriver.Chrome(executable_path='C:\\Study\\Python\\tgBot\\parsers\\chromedriver\\chromedriver.exe', options=options)
driver.implicitly_wait(10)


def main():
  try:
    driver.get(url=url)
    offers = get_offers()
    #pages = driver.find_element(
        #By.XPATH, '//nav[@aria-label="Пагинация"]/ul/li[8]/a[contains(@class, "styles-module-item_last")]/span').text
    #pages = int(pages)
    #print(pages)
    #for page in range(15,pages+1):
        #driver.get(f'https://www.avito.ru/moskva/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?f=ASgBAQICAkSSA8gQ8AeQUgFA7MENNIbPOYTPOYLPOQ&p={page}&s=104&user=1')
        #print(f"Переход на страницу {page}")
        #offers = get_offers()
  except Exception as ex:
    print(ex)
  finally:
      driver.close()
      driver.quit()


def get_offer(item, offer_index):
    try:
        item[offer_index].click()
        driver.switch_to.window(driver.window_handles[1])
        offer = {}
        title = driver.find_element(
        By.CLASS_NAME, 'title-info-title-text').text
        offer['title'] = title
        price = driver.find_element(
            By.XPATH, '//div[contains(@class, "style-item-view-price-content")]/div/div/div/div/span/span/span[@itemprop="price"]').text
        price = price.replace(' ', '')
        offer['price'] = int(price)
        offer['url'] = driver.current_url
        offer_id = driver.find_element(
            By.XPATH, '//article[contains(@class, "style-item-footer-text")]/p/span[@data-marker="item-view/item-id"]').text
        offer['offer_id'] = int(offer_id[2:])
        date = driver.find_element(
            By.XPATH, '//article[contains(@class, "style-item-footer-text")]/p/span[@data-marker="item-view/item-date"]').text
        date = date[2:].split()
        if 'сегодня' in date:
            today = datetime.strftime(datetime.today(), '%Y-%m-%d')
            publication_time = today + ' ' + date[-1] + ':00'
            offer['offer_date'] = publication_time
        elif 'вчера' in date:
            yesterday = datetime.today() - timedelta(days=1)
            yesterday = datetime.strftime(yesterday, '%Y-%m-%d')
            publication_time = yesterday + ' ' + date[-1] + ':00'
            offer['offer_date'] = publication_time
        else:
            publication_time = '2023' + '-' + month[date[1]] + '-' + date[0] + ' ' + date[-1] + ':00'
            offer['offer_date'] = publication_time
        title_elements = title.split(', ')
        area = title_elements[1].split(' ')
        if ',' in area[0]:
            area = area[0].replace(',', '.')
            offer['area'] = float(area)
        else:
            offer['area'] = float(area[0])
        if 'студия' in title_elements[0]:
            offer['rooms'] = 0
        else:
            rooms = title_elements[0].split(' ')
            rooms = rooms[0].split('-')
            offer['rooms'] = int(rooms[0])
        offer['address'] = driver.find_element(
            By.XPATH, '//div[contains(@class, "style-item-address")]/div/span').text
        try:
            offer['undergrounds'] = driver.find_element(
                By.XPATH, '//div[contains(@class, "style-item-address")]/div/div/span/span/span[2]').text
        except Exception as ex:
            offer['undergrounds'] = ''
        floor = title_elements[2].split('/')
        offer['floor'] = int(floor[0])
        check_database(offer)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.switch_to.window(driver.window_handles[0])


def get_offers():
    items = driver.find_elements(By.XPATH, '//div[@data-marker="item"]/div/div/div[1]/a/div[@data-marker="item-photo"]')
    for offer_index in range(len(items)):
       offer = get_offer(items, offer_index)



def check_database(offer):
    with sqlite3.Connection("./db/realty.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT offer_id FROM offers WHERE offer_id = (?)
        """, (offer['offer_id'], ))
        result = cursor.fetchone()
        if result is None:
            cursor.execute("""
                INSERT INTO offers
                VALUES (NULL, :title, :price, :url, :offer_id, :offer_date, :area, :rooms, :address, :undergrounds, :floor)
            """, offer)
            connection.commit()
            print(f"Объявление {offer['offer_id']} добавлено в базу данных")
            print('--------------------------------')
    
   


if __name__ == '__main__':
    main()