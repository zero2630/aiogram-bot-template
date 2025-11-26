import asyncio  # noqa: F401

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext

from app.bot.keyboards import reply, inline
from app.services import user, user_settings, note
from app.bot.states.default_states import CreateNoteState

router = Router()


@router.message(F.text == "Смотреть заметки")
async def watch_notes(message: Message, state: FSMContext):
    data = await note.get_note(0)
    if data:
        notes_amount = await note.get_notes_amount()
        await message.answer(
        f"<b>{data.title}</b>\n{data.text}",
        reply_markup=inline.get_pagination_kb(1, notes_amount, "note"),
        )
    else:
        await message.answer("Нет заметок", reply_markup=reply.get_main_menu())


@router.callback_query(inline.Paginator.filter(F.action.startswith("note") & F.action.endswith(("prev", "next"))))
async def callback_watch_notes(call: CallbackQuery, callback_data: inline.UserSettings):
    data = await note.get_note(callback_data.page-1)

    await call.message.edit_text(
    f"<b>{data.title}</b>\n{data.text}",
    reply_markup=inline.get_pagination_kb(callback_data.page, callback_data.total_pages, "note"),
    )
