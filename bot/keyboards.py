from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


filters_buttons = ["Метро", "Цена", "Комнаты", "Площадь"]
filters_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
filters_keyboard.add(filters_buttons[0], filters_buttons[1]).add(filters_buttons[2], filters_buttons[3])

#result_buttons = ["Показать еще", "Вернуться к фильтрам"]
#result_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#result_keyboard.add(result_buttons[0], result_buttons[1])