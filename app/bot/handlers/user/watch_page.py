import asyncio  # noqa: F401

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext

from app.bot.keyboards import reply, inline
from app.services import user, user_settings, page
from app.bot.states.default_states import CreatePageState

router = Router()


@router.message(F.text == "смотреть страницы")
async def watch_pages(message: Message, state: FSMContext):
    data = await page.get_page(0)
    pages_amount = await page.get_pages_amount()
    await message.answer(
    f"<b>{data.title}</b>\n{data.text}",
    reply_markup=inline.get_pagination_kb(1, pages_amount, "note"),
    )


@router.callback_query(inline.Paginator.filter(F.action.startswith("note") & F.action.endswith(("prev", "next"))))
async def callback_watch_pages(call: CallbackQuery, callback_data: inline.UserSettings):
    data = await page.get_page(callback_data.page-1)

    await call.message.edit_text(
    f"<b>{data.title}</b>\n{data.text}",
    reply_markup=inline.get_pagination_kb(callback_data.page, callback_data.total_pages, "note"),
    )
