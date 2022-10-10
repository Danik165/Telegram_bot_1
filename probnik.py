from aiogram.types import Message

from config import admin_id
from main import bot, dp
from weather_2 import current_temperature, weather_description, current_humidity


async def send_to_admin(d):
    await bot.send_message(chat_id=admin_id, text='Bot is on:1')


@dp.message_handler()
async def ans(message: Message):
    text = 'Ваше сообщение очень важно для нас, мы вернемся с ответом, когда у нас будут руки, а не лапки'
    answ = message.from_user.id
    await bot.send_message(chat_id=admin_id,
                           text=str(answ) + '\n' + message.text)
    # await bot.send_message(chat_id=message.from_user.id, text='w', disable_notification=True)
    await message.answer(
        text=str(current_temperature) + '\n' + str(weather_description) + '\n' + str(current_humidity) + '%')
