import asyncio
from aiogram import Bot, Dispatcher
from registration import registration
from menu import menu
from stip import stipend
from ivent import event
from vopr_v_raspis import voprosik
from dock import docki
from admin import admin
from r_raspis import raspis
async def main():
    TOKEN_API = "6662629827:AAHoIxMjnrbtSLX2W7Pw3ARqbAjf_xq8QbI"
    bot = Bot(TOKEN_API)
    dp = Dispatcher()
    dp.include_router(menu)
    dp.include_router(registration)
    dp.include_router(stipend)
    dp.include_router(voprosik)
    dp.include_router(event)
    dp.include_router(docki)
    dp.include_router(admin)
    dp.include_router(raspis)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())