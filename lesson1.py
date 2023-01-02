from aiogram import Bot, Dispatcher, executor, types

# Бот - сервер, который будет взаимодействовать с API Telegram
TOKEN_API = "5602277457:AAGyHQwtGu-ZC1K1j01bVvZAqcqTz7fV4hg" # Авторизационный токен для подключения к Telegram API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text) # Написать сообщение


if __name__ == '__main__':
    executor.start_polling(dp)
