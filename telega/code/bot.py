import asyncio
from aiogram import Bot, Dispatcher
from registration import registration
from menu import menu
from stip import stipend
from vopr_v_raspis import voprosik
from dock import docki
from admin import admin
from r_raspis import raspis


async def main():
    TOKEN_API = "7503899100:AAEcNx9fksbRf2pjOfIRLXf6ZtaLT0fb6BU"
    bot = Bot(TOKEN_API)
    dp = Dispatcher()
    dp.include_router(menu)
    dp.include_router(registration)
    dp.include_router(stipend)
    dp.include_router(voprosik)
    dp.include_router(docki)
    dp.include_router(admin)
    dp.include_router(raspis)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())









