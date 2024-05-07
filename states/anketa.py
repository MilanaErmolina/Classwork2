"""Module providing a function printing python version."""
from aiogram.fsm.state import State, StatesGroup


class Anketa(StatesGroup):
    """Class representing a person"""
    name = State()
    age = State()
    gender = State()
