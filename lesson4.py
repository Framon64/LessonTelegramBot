from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# Бот - сервер, который будет взаимодействовать с API Telegram
TOKEN_API = "5602277457:AAGyHQwtGu-ZC1K1j01bVvZAqcqTz7fV4hg" # Авторизационный токен для подключения к Telegram API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
kp1 = ReplyKeyboardMarkup(resize_keyboard=True)
kp = ReplyKeyboardMarkup(resize_keyboard=True)# !
kp.add(KeyboardButton('/help'))
kp1.add(KeyboardButton('/start'))


HELP_COMMAND = '''
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>старт бота</em>
<b>/description</b> - <em>описание бота</em>
<b>/photo</b> - <em>отправка фото</em> 
'''


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND, parse_mode='HTML', reply_markup=ReplyKeyboardRemove())
    await message.delete()

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='Добро пожаловать в наш бот', parse_mode='HTML', reply_markup=kp)
    await message.delete()

@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.answer(text='Наш бот умеет отправлять фотографии', parse_mode='HTML')
    await message.delete()

@dp.message_handler(commands=['photo'])
async def photo_command(message: types.Message):
    await message.answer_photo(photo='https://krasivosti.pro/uploads/posts/2022-08/1659368049_40-krasivosti-pro-p-kotiki-grustnie-krasivo-foto-53.jpg', parse_mode='HTML')
    await message.delete()




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
