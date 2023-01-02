from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = "5602277457:AAGyHQwtGu-ZC1K1j01bVvZAqcqTz7fV4hg"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот был запущен!')

@dp.message_handler(commands=['start'])
async def tart_command(message: types.Message):
    await message.answer('<em>Привет, добро пожаловать в наш бот!</em>', parse_mode="HTML")


@dp.message_handler(commands=['give'])
async def tart_command(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker="CAACAgEAAxkBAAEHGgdjsytjCEk1fyV4iG5Msy4E9TGZ7wACmg8AApl_iAK_5GAhI10aZi0E")
    await message.delete()

@dp.message_handler()
async def send_emoji(message: types.Message):
     await message.answer(message.text + '😳')



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

