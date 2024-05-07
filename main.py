"""Module providing a function printing python version."""
import asyncio

from aiogram import Bot, Dispatcher
from handlers import include_routers

bot = Bot(token="7157439516:AAHTbVmmNgfIu4L0iLJSkBjfqORLcvXZ_tY")
dp = Dispatcher()


async def main():
    """Function printing python version."""
    include_routers(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
