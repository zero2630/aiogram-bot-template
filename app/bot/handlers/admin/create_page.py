import asyncio  # noqa: F401

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext

from app.bot.keyboards import reply, inline
from app.services import user, user_settings, page
from app.bot.states.default_states import CreatePageState
from app.bot.filters import admin_filter

router = Router()
router.message.filter(admin_filter.AdminFilter())


@router.message(F.text == "создать страницу")
async def create_page_start(message: Message, state: FSMContext):
    await state.set_state(CreatePageState.title)
    await message.answer(
    "Напишите название",
    reply_markup=reply.get_main_menu(),
    )


@router.message(CreatePageState.title, F.text)
async def create_page_title(message: Message, state: FSMContext):
    await state.set_state(CreatePageState.text)
    await state.update_data(title=message.text)
    await message.answer(
        "Напишите текст",
        reply_markup=reply.get_main_menu(),
    )


@router.message(CreatePageState.text, F.text)
async def create_page_title(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    data = await state.get_data()
    await state.clear()
    await page.create_page(data["title"], data["text"])
    await message.answer(
        "Страница добавлена",
        reply_markup=reply.get_main_menu(),
    )
