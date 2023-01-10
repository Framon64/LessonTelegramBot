from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Бот - сервер, который будет взаимодействовать с API Telegram
TOKEN_API = "5602277457:AAGyHQwtGu-ZC1K1j01bVvZAqcqTz7fV4hg" # Авторизационный токен для подключения к Telegram API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kp = InlineKeyboardMarkup(row_width=2)
kp_button_1 = InlineKeyboardButton(text="Кнопка 1", url='https://metanit.com/python/tutorial/')
kp_button_2 = InlineKeyboardButton(text="Кнопка 2", url='https://metanit.com/python/tutorial/')

kp.add(kp_button_1, kp_button_2)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text="Привет Мир!", reply_markup=kp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)