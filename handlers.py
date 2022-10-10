from aiogram.types import Message

from config import admin_id
from main import bot, dp


async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text='Bot is on:2')


@dp.message_handler()
async def ans(message: Message):
    text = 'Ваше сообщение очень важно для нас, мы вернемся с ответом, когда у нас будут руки, а не лапки'
    await bot.send_message(chat_id=admin_id,
                           text=str(message.from_user.id) + '\n' + message.text)
    await message.answer(text=text)
    if message.from_user.id == '394761402':
        message.answer(text='f')


@dp.message_handler()
async def sec(message: Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='буй')
