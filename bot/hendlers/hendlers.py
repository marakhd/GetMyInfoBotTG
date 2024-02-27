#import aiogram
from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
import config as cfg

router = Router()

#Хендлер старт
@router.message(CommandStart())
async def start(message: types.Message):
    prem = message.from_user.is_premium
    if (prem == True):
        prem = 'Подключена'
    else:
        prem = 'Отключено'

    await message.answer(f'Привет {message.from_user.full_name} ✋')
    await message.answer(f'Твой ID: <code>{message.from_user.id}</code> '
                         f'\nЮзернейм: @{message.from_user.username}'
                         f'\nСтатус TG Premium: {prem}')
#Хендлер get
@router.message((Command('get') or Command('id')))
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
                        f'\nТвой ID: <code>{message.from_user.id}</code> '
                         f'\nЮзернейм: @{message.from_user.username}'
                         f'\nСтатус TG Premium: {prem}')

#хендлер на хелп
@router.message(Command('help'))
async def help_user(message: types.Message):
    await message.answer(f'Этот бот позволяет получить User ID. '
                         f'\nНапишите боту команду /get чтобы получить инфо о своём профиле.'
                         f'\n\nЕсли вы хотите узнать ID другого человека, то просто перешлите боту сообщение которое написал этот человек. '
                         f'\n\nВы можете узнать ID стикера, просто отправьте стикер боту'
                         f'\n\nUser ID - это ваш уникальный идентификатор в Telegram который вы можете использовать в своем боте'
                         f'\n\n<a href="https://core.telegram.org/bots/api#user">Подробнее</a>', disable_web_page_preview = True)

#Хендлер для команды why
@router.message(Command("why"))
async def start(message: types.Message):
    await message.answer(f'Мы OpenSource проект телеграм бота!'
                         f'\nЭтот бот помогает вам создать своего бота. Подробнее /help'
                         f'\n\nВы можете наблюдать за разработкой на нашем <a href="{cfg.GITHUB}">GitHub</a>', disable_web_page_preview = False)

#Хендлер на текст
@router.message(F.text)
async def all_msg(message: types.Message):
    if (message.from_user.is_premium == True):
        prem = 'Подключена'
    else:
        prem = 'Отключено'
    name = message.from_user.first_name
    if (name == None):
        name = 'Нет'
    surname = message.from_user.last_name
    if (surname == None):
        surname = 'Нет'
    if (message.forward_from != None):
        if (message.forward_from.is_premium == True):
            premforward = 'Подключена'
        else:
            premforward = 'Отключено'
        nameforward = message.from_user.first_name
        if (nameforward == None):
            nameforward = 'Нет'
        surnameforward = message.from_user.last_name
        if (surnameforward == None):
            surnameforward = 'Нет'
        await message.answer(f'Ваше имя: {name}'
                            f'\nВаша фамилия: {surname}'
                            f'\nТвой ID: <code>{message.from_user.id}</code> '
                            f'\nТвой юзернейм: @{message.from_user.username}'
                            f'\nТвой статус TG Premium: {prem}')
        await message.reply(f'Имя из сообщения: {nameforward}'
                            f'\nФамилия из сообщения: {surnameforward}'
                            f'\nID из сообщения: <code>{message.forward_from.id}</code> '
                            f'\nЮзернейм из сообщения: @{message.forward_from.username}'
                            f'\nСтатус TG Premium из сообщения: {premforward}')
    else:
        await message.reply(f'Имя: {name}'
                            f'\nФамилия: {surname}'
                            f'\nТвой ID: <code>{message.from_user.id}</code> '
                            f'\nЮзернейм: @{message.from_user.username}'
                            f'\nСтатус TG Premium: {prem}')

#Хендлер на стикеры
@router.message(F.sticker)
async def sticker(message: types.Message):
    await message.reply(f'ID стикера:'
                        f'\n<code>{message.sticker.file_id}</code>'
                        f'\n\nЧтобы узнать информацию о себе напишите /get')

#Хендлер на все
@router.message()
async def error(message: types.Message):
    await message.answer(f'Ошибка')
    await message.answer(f'Бот принимает только текст и стикеры')