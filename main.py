#Import config
import config as cfg
#import logging and asyncio
import logging
import asyncio
#import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
#on logging (debug)
logging.basicConfig(level=logging.INFO)
#init bot
bot = Bot(token=cfg.TOKEN)
dp = Dispatcher()
#Хендлер старт
@dp.message(CommandStart())
async def start(message: types.Message):
    prem = message.from_user.is_premium
    if (prem == True):
        prem = 'Подключена'
    else:
        prem = 'Отключено'

    await message.answer(f'Привет {message.from_user.full_name} ✋')
    await message.answer(f'Твой ID: {message.from_user.id} '
                         f'\nЮзернейм: @{message.from_user.username}'
                         f'\nСтатус TG Premium: {prem}')
#Хендлер get
@dp.message(Command('get'))
async def get(message: types.Message):
    prem = message.from_user.is_premium
    if (prem == True):
        prem = 'Подключена'
    else:
        prem = 'Отключено'

    name = message.from_user.first_name
    if (name == None):
        name = 'Нет'

    surname = message.from_user.last_name
    if (surname == None):
        surname = 'Нет'

    await message.answer(f'Имя: {name}'
                        f'\nФамилия: {surname}'
                        f'\nТвой ID: {message.from_user.id} '
                         f'\nЮзернейм: @{message.from_user.username}'
                         f'\nСтатус TG Premium: {prem}')

#хендлер на хелп
@dp.message(Command('help'))
async def help(message: types.Message):
    await message.answer(f'Этот бот позволяет получить User ID. '
                         f'\nНапишите боту команду /get чтобы получить инфо о своём профиле')

#Хендлер на все
@dp.message()
async def all(message: types.Message):
    prem = message.from_user.is_premium
    if (prem == True):
        prem = 'Подключена'
    else:
        prem = 'Отключено'

    name = message.from_user.first_name
    if (name == None):
        name = 'Нет'

    surname = message.from_user.last_name
    if (surname == None):
        surname = 'Нет'

    await message.reply(f'Имя: {name}'
                        f'\nФамилия: {surname}'
                        f'\nТвой ID: {message.from_user.id} '
                        f'\nЮзернейм: @{message.from_user.username}'
                        f'\nСтатус TG Premium: {prem}')

#Пулинг бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())

    except (KeyboardInterrupt):
        print('off bot')