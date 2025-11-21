import asyncio  # noqa: F401

from aiogram.filters import Command
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.bot.keyboards import reply, inline
from app.bot.states.default_states import CreateBroadcast
from app.services import broadcast
from app.bot.filters import admin_filter

router = Router()
router.message.filter(admin_filter.AdminFilter())


@router.message(Command("admin"))
async def command_admin(message: Message):
    await message.answer(
        "admin mode",
        reply_markup=reply.get_admin_menu(),
    )


@router.message(F.text == "рассылка")
async def create_broadcast_start(message: Message, state: FSMContext):
    await state.set_state(CreateBroadcast.text)
    await message.answer(
    "Введите текст рассылки",
    reply_markup=reply.get_admin_menu(),
    )


@router.message(CreateBroadcast.text, F.text)
async def create_broadcast_text(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
    f"Ваш текст:\n<blockquote>{message.text}</blockquote>",
    reply_markup=inline.get_broadcast_confirm_kb(message.text),
    )


@router.callback_query(inline.Broadcast.filter(F.action == "send"))
async def send_broadcast_callback(call: CallbackQuery, callback_data: inline.Broadcast):
    await call.answer("Отправлено")
    await call.message.delete()
    await broadcast.create_and_send_broadcast(callback_data.text, call.bot)


@router.callback_query(inline.Broadcast.filter(F.action == "cancel"))
async def send_broadcast_callback(call: CallbackQuery, callback_data: inline.Broadcast):
    await call.answer("Отменено")
    await call.message.delete()
