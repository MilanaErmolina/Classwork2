"""Module providing a function printing python version."""
from aiogram import Dispatcher

from handlers import anketa, start

def include_routers(dp: Dispatcher):
    """Function printing python version."""
    dp.include_routers(
        start.router,
        anketa.ruoter
        )
