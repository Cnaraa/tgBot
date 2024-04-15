import pandas as pd
import matplotlib.pyplot as plt
from conversion_to_dataframe import conversion_to_df

df = conversion_to_df()

metro_stations = df['undergrounds'].str.split(
    ',').explode().str.strip().value_counts()
metro_stations = metro_stations.head(10)
plt.bar(metro_stations.index, metro_stations.values)
plt.xlabel('Станции метро')
plt.ylabel('Количество объявлений')
plt.title('Частота объявлений')
plt.xticks(rotation=30)
plt.show()

#Гистограмма кол-ва объявлений по комантам
df['rooms'].value_counts().plot(kind='bar')
plt.xlabel('Количество комнат')
plt.ylabel('Количество объявлений')
plt.title('Распределение количества комнат')
plt.show()

#Построения графика количества объявлений по дате размещения
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df.resample('D').size().plot()
plt.xlabel('Дата')
plt.ylabel('Количество объявлений')
plt.title('Распределение объявлений по дате')
plt.show()

#Построение диограммы рессеяния цены и площади
plt.scatter(df['area'], df['price'])
plt.xlabel('Площадь')
plt.ylabel('Цена')
plt.title('Распределение цен в зависимости от площади')
plt.show()

#Статистика по районам
popular_districts = df['address'].str.split(',').value_counts().head(10)
popular_districts.plot(kind='bar')
plt.xlabel('Районы')
plt.ylabel('Количество объявлений')
plt.title('Статистика по районам')
plt.xticks(rotation=45)
plt.show()

#График самых дорогих районов
mean_price_by_area = df.groupby('address')['price'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
mean_price_by_area.plot(kind='bar')
plt.xlabel('Район')
plt.ylabel('Средняя арендная цена')
plt.title('Средняя арендная цена по районам')
plt.xticks(rotation=45)
plt.show()
