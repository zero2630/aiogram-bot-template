from aiogram.fsm.state import StatesGroup, State


class DefaultState(StatesGroup):
    state1 = State()
    state2 = State()
    state3 = State()


class CreatePageState(StatesGroup):
    title = State()
    text = State()
