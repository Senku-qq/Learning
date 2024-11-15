from aiogram import Bot , Dispatcher 
import asyncio
from TOKEN import TOKEN_API
import logging
from handlers import router
Token_connect = TOKEN_API
bot = Bot(token=Token_connect)
dp = Dispatcher()

async def main ():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
