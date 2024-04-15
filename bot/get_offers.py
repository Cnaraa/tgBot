import sqlite3


UNDERGROUNDS_UPPER_NAME = ['ВДНХ', 'ЗИЛ', 'ЦСКА']


def get_offers(data):
    with sqlite3.connect("./db/realty.db") as connection:
        cursor = connection.cursor()
        if data.get('underground'):
          if data.get('underground') in UNDERGROUNDS_UPPER_NAME:
            underground = '%' + data['underground'] + '%'
          else:
            underground = '%' + data['underground'].title() + '%'
          cursor.execute('''
            SELECT title, price, url, date, address, undergrounds FROM offers WHERE undergrounds like (?) ORDER BY strftime('%Y-%m-%d %H:%M:%S', date) DESC
          ''', (underground, ))
          result = cursor.fetchmany(size=5)
          return result
        elif data.get('price'):
          price = data['price']
          cursor.execute('''  
            SELECT title, price, url, date, address, undergrounds FROM offers WHERE price <= (?) ORDER BY strftime('%Y-%m-%d %H:%M:%S', date) DESC
            ''', (price, ))
          result = cursor.fetchmany(size=5)
          return result
        elif data.get('area'):
          try:
            min_area = float(data['area'][0])
            max_area = float(data['area'][1])
            cursor.execute('''
              SELECT title, price, url, date, address, undergrounds FROM offers WHERE area >= (?) AND area <= (?) ORDER BY strftime('%Y-%m-%d %H:%M:%S', date) DESC
              ''', (min_area, max_area))
            result = cursor.fetchmany(size=5)
            return result
          except (IndexError, ValueError):
             return "Некорректные данные. Снова выберите фильтр 'Площадь' и введите 2 значения через пробел (только числа). Первое - минимальная, второе - максимальная площадь"
        elif data.get('rooms'):
          rooms_count = int(data['rooms'])
          cursor.execute('''
            SELECT title, price, url, date, address, undergrounds FROM offers WHERE rooms = (?) ORDER BY strftime('%Y-%m-%d %H:%M:%S', date) DESC
          ''', (rooms_count, ))
          result = cursor.fetchmany(size=5)
          return result
           
