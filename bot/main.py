#Import config
import config as cfg
#import logging and asyncio
import logging
import asyncio
#import aiogram
from aiogram import Bot, Dispatcher
from hendlers.hendlers import router

#on logging (debug)
logging.basicConfig(level=logging.INFO)

#init bot
bot = Bot(token=cfg.TOKEN, parse_mode='HTML')
dp = Dispatcher()

#Пулинг бота
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())

    except (KeyboardInterrupt):
        print('off bot')