from aiogram import Bot, Dispatcher, executor, types

HELP_COMMAND = '''
/help - список команд
/start - нвчать работу с ботом    
'''

# Бот - сервер, который будет взаимодействовать с API Telegram
TOKEN_API = "5602277457:AAGyHQwtGu-ZC1K1j01bVvZAqcqTz7fV4hg" # Авторизационный токен для подключения к Telegram API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['help'])
async def help_message(message: types.Message): 
    await message.reply(text=HELP_COMMAND)

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message): 
    await message.reply(text="Добро пожаловать в наш Телеграмм бот")
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp)
