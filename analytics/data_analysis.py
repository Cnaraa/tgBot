import numpy as np
import pandas as pd
import re
from conversion_to_dataframe import conversion_to_df

df = conversion_to_df()


#Вывод разных групп рядов и колонок объекта df
print(df.head(5))
print(df['title'])
print(df[['title', 'price']])


#Очистка "Цифрового мусора"
df['undergrounds'] = df['undergrounds'].apply(lambda x: 'No' if re.search(r'^\s*$', str(x)) else x)
#print(df['undergrounds'].value_counts())


#Рассчет статистических характеристик и запись в файл
price_status = df['price'].describe()
area_status = df['area'].describe()
price_median = df['price'].median()
area_median = df['area'].median()
print(price_status)
print(area_status)
print(area_median)
print(price_median)

with open('general_statistics.txt', 'w') as file:
    file.write('Средние  значения для цены:\n')
    file.write(str(price_status))
    file.write('\n-----------------------------')
    file.write('\nСредние  значения для площади:\n')
    file.write(str(area_status))
    file.write('\n-----------------------------')
    file.write('\nМедиана для цены:\n')
    file.write(str(price_median))
    file.write('\n-----------------------------')
    file.write('\nМедиана для площади:\n')
    file.write(str(area_median))


#Добавление новых колонок на основе статистических вычислений
df = df.assign(PRICE_MEAN=df['price'].mean(), AREA_MEDIAN=df['area'].median())
print(df.head(10))


#Способы разделения данных по разным признакам
mean_price_by_rooms = df.groupby('rooms')['price'].mean()
metro_stations = df['undergrounds'].str.split(',').explode().str.strip().value_counts()
popular_districts = df['address'].str.split(',').value_counts()

df_subset = df[['price', 'area']]  # Корреляция между ценой и площадью
correlation = df_subset.corr()

quantiles = pd.qcut(df['price'], q=3, labels=['Low', 'Medium', 'High']) # Создание категорий на основе квантилей
df['Price_Category'] = quantiles

#print(df['Price_Category'].value_counts())
#print(mean_price_by_rooms)
#print(metro_stations)
#print(popular_districts)
#print(correlation)

df['Price_per_Sqm'] = df['price'] / df['area']
Economic_expediency = pd.qcut(df['Price_per_Sqm'], q=3, labels=['Low', 'Medium', 'High']) #Разделение по экономической целесообразности (Цена за кв.м)
df['Economic_expediency'] = Economic_expediency
#print(df['Economic_expediency'].value_counts())

#Создание отчета по новым способам разделения данных
with open('split_data_statistics.txt', 'w') as file:
    file.write('Средние  значения цены по количеству комнат:\n')
    file.write(str(mean_price_by_rooms))
    file.write('\n-----------------------------')
    file.write('\nСтатистика по станциям метро:\n')
    file.write(str(metro_stations))
    file.write('\n-----------------------------')
    file.write('\nСтатистика по районам:\n')
    file.write(str(popular_districts))
    file.write('\n-----------------------------')
    file.write('\nКорреляция между ценой и площадью:\n')
    file.write(str(correlation))
    file.write('\n-----------------------------')
    file.write('\nРазделение цены по 3 категориям:\n')
    file.write(str(df['Price_Category'].value_counts()))
    file.write('\n-----------------------------')
    file.write('\nРазделение по экономической целесообразности:\n')
    file.write(str(df['Economic_expediency'].value_counts()))

# Пример объединения сгенерированных статистических данных
df = pd.merge(df, mean_price_by_rooms, on='rooms', how='left')
#df = pd.merge(df, metro_stations, left_on='undergrounds', right_index=True, how='left')

#print(df.head(100))
df.to_csv('realty.csv', index=False)

#Гипотезы
#Предсказание цены по площади и количеству комнат
def predict_price(area, rooms):
    X = df[['area', 'rooms']]
    y = df['price_x']

    X = np.column_stack((np.ones(len(X)), X))

    # Вычисляем коэффициенты регрессии с использованием метода наименьших квадратов
    coef, _, _, _ = np.linalg.lstsq(X, y, rcond=None)

    # Прогнозируем цену и вводим новые значения признаков для прогноза
    X_pred = np.array([1, area, rooms])
    y_pred = X_pred @ coef

    # Вычисляем среднеквадратичную ошибку
    y_pred_all = X @ coef
    rmse = np.sqrt(np.mean(np.square(y - y_pred_all)))

    return y_pred, rmse
price_pred, rmse = predict_price(50, 2)
print(f'Прогнозируемая цена = {price_pred}')
print(f'Среднеквадратичная ошибка = {rmse}')
