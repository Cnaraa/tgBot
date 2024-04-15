from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from keyboards import *
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hbold, hlink
import time  # enumerate
from get_offers import get_offers


storage = MemoryStorage()
bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)


class Filters(StatesGroup):

   undeground = State()
   price = State()
   area = State()
   rooms = State()


async def on_startup(_):
   print("Бот успешно запущен!") #Сообщение в терминал


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
  await bot.send_message(chat_id=message.from_user.id,
                         text="Привет!👋 Я помогу вам найти подходящую квартиру по вашим требованиям.🏡\nДля поиска объявлений воспользуйтесь встроенной клавиатурой",
                         reply_markup=filters_keyboard)
  await message.delete()


@dp.message_handler(Text(equals='Метро'))
async def undeground_filter(message: types.Message):
   await message.answer('Введите название станции')
   await Filters.undeground.set()


@dp.message_handler(Text(equals='Цена'))
async def undeground_filter(message: types.Message):
   await message.answer('Введите ваш бюджет')
   await Filters.price.set()


@dp.message_handler(Text(equals='Площадь'))
async def undeground_filter(message: types.Message):
   await message.answer('Введите минимальную и максимальную площадь квартиры через пробел. Например: 20 40')
   await Filters.area.set()


@dp.message_handler(Text(equals='Комнаты'))
async def undeground_filter(message: types.Message):
   await message.answer('Введите количество комнат. (0 - Студия)')
   await Filters.rooms.set()


@dp.message_handler(state=Filters.undeground)
async def get_offers_on_underground(message: types.Message, state : FSMContext):
   async with state.proxy() as data:
      data['underground'] = message.text.upper()
      offers = get_offers(data)
      if len(offers) == 0:
         await message.answer('По такому запросу объявления еще не разместили')
      else:
         for index, offer in enumerate(offers):
            card = f'{hlink(offer[0], offer[2])}\n'\
                  f'{hbold("Цена: ")}{offer[1]}\n'\
                  f'{hbold("Адресс: ")}{offer[4]}\n'\
                  f'{hbold("Метро: ")}{offer[5]}\n'\
                  f'{hbold("Дата публикации: ")}{offer[3]}\n'
            await message.answer(card)
            
   await state.finish()


@dp.message_handler(state=Filters.price)
async def get_offers_on_price(message: types.Message, state: FSMContext):
   async with state.proxy() as data:
      try:
         data['price'] = int(message.text)
         offers = get_offers(data)
         if len(offers) == 0:
            await message.answer('По такому запросу объявления еще не разместили')
         else:
            for index, offer in enumerate(offers):
               card = f'{hlink(offer[0], offer[2])}\n'\
                  f'{hbold("Цена: ")}{offer[1]}\n'\
                  f'{hbold("Адресс: ")}{offer[4]}\n'\
                  f'{hbold("Метро: ")}{offer[5]}\n'\
                  f'{hbold("Дата публикации: ")}{offer[3]}\n'
               await message.answer(card)
            #data['offers'] = offers
            #data['page'] = 1
            #await state.update_data(offers=offers, page=1)
            #await show_next_offers(message, state, storage)
      except ValueError:
         await message.answer("Некорректные данные. Снова выберите фильтр 'Цена' и введите только сумму без пробелов и символов")
   await state.finish()

'''
async def show_next_offers(message: types.Message, state: FSMContext, storage: MemoryStorage):
   async with state.proxy() as data:
      offers = offers.get('offers', [])
      page = data.get('page', 1)
      start_index = (page - 1) * 5
      end_index = start_index + 5
      current_offers = offers[start_index:end_index]
      for offer in current_offers:
          card = f'{hlink(offer[0], offer[2])}\n'\
              f'{hbold("Цена: ")}{offer[1]}\n'\
              f'{hbold("Адресс: ")}{offer[4]}\n'\
              f'{hbold("Метро: ")}{offer[5]}\n'\
              f'{hbold("Дата публикации: ")}{offer[3]}\n'
          await message.answer(card)
      if end_index < len(offers):
         await message.answer('Вот что удалось найти', reply_markup=result_keyboard)
      else:
         await message.answer('Вот что удалось найти')


@dp.message_handler(Text(equals='Показать еще'))
async def show_more_offers(message: types.Message, state: FSMContext):
   async with state.proxy() as data:
      page = data.get('page', 1)
      data['page'] = page + 1
      #await state.update_data(page=page + 1)
      #await state.update_data(offers=data['offers'])
      await show_next_offers(message, state, storage)


@dp.message_handler(Text(equals='Вернуться к фильтрам'))
async def retrun_to_filters(message: types.Message, state: FSMContext):
   async with state.proxy() as data:
      await state.finish()
      await message.answer("Выберите фильтр для поиска", reply_markup=filters_keyboard)
      await message.delete()
'''

@dp.message_handler(state=Filters.area)
async def get_offers_on_area(message: types.Message, state: FSMContext):
   async with state.proxy() as data:
      data['area'] = message.text.split()
      offers = get_offers(data)
      if isinstance(offers, str):
         await message.answer(offers)
      elif len(offers) == 0:
         await message.answer('По такому запросу объявления еще не разместили')
      else:
         for index, offer in enumerate(offers):
            card = f'{hlink(offer[0], offer[2])}\n'\
               f'{hbold("Цена: ")}{offer[1]}\n'\
               f'{hbold("Адресс: ")}{offer[4]}\n'\
               f'{hbold("Метро: ")}{offer[5]}\n'\
               f'{hbold("Дата публикации: ")}{offer[3]}\n'
            await message.answer(card)
   await state.finish()


@dp.message_handler(state=Filters.rooms)
async def get_offers_on_rooms(message: types.Message, state: FSMContext):
   async with state.proxy() as data:
      try:
         data['rooms'] = message.text
         offers = get_offers(data)
         if len(offers) == 0:
            await message.answer('По такому запросу объявления еще не разместили')
         for index, offer in enumerate(offers):
            card = f'{hlink(offer[0], offer[2])}\n'\
               f'{hbold("Цена: ")}{offer[1]}\n'\
               f'{hbold("Адресс: ")}{offer[4]}\n'\
               f'{hbold("Метро: ")}{offer[5]}\n'\
               f'{hbold("Дата публикации: ")}{offer[3]}\n'
            await message.answer(card)
      except ValueError:
         await message.answer("Некорректные данные. Снова выберите фильтр 'Комнаты' и введите только число комнат. (0 - Студия)")
   await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True) #запуск бота