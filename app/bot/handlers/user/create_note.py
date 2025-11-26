import asyncio  # noqa: F401

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext

from app.bot.keyboards import reply, inline
from app.services import user, user_settings, note
from app.bot.states.default_states import CreateNoteState
from app.bot.filters import admin_filter

router = Router()
router.message.filter()


@router.message(F.text == "Создать заметку")
async def create_note_start(message: Message, state: FSMContext):
    await state.set_state(CreateNoteState.title)
    await message.answer(
    "Напишите название",
    reply_markup=reply.get_main_menu(),
    )


@router.message(CreateNoteState.title, F.text)
async def create_note_title(message: Message, state: FSMContext):
    await state.set_state(CreateNoteState.text)
    await state.update_data(title=message.text)
    await message.answer(
        "Напишите текст",
        reply_markup=reply.get_main_menu(),
    )


@router.message(CreateNoteState.text, F.text)
async def create_note_title(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    data = await state.get_data()
    await state.clear()
    await note.create_note(data["title"], data["text"])
    await message.answer(
        "Страница добавлена",
        reply_markup=reply.get_main_menu(),
    )
