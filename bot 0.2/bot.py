import asyncio
from aiogram import Bot, Dispatcher
from router import router
async def main():
    TOKEN_API = "6662629827:AAHoIxMjnrbtSLX2W7Pw3ARqbAjf_xq8QbI"
    bot = Bot(TOKEN_API)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())