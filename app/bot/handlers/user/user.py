import asyncio  # noqa: F401

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart

from app.bot.keyboards import reply, inline
from app.services import user, user_settings

router = Router()


@router.message(CommandStart())
async def command_start(message: Message, command: Command):
    await user.create_user(message.from_user.id)
    await message.answer(
        "Стартовый текст",
        reply_markup=reply.get_main_menu(),
    )


@router.message(F.text == "настройки")
async def settings(message: Message):
    await message.answer(
    "настройки",
    reply_markup=(await inline.get_user_settings_kb(message.from_user.id))
    )


@router.callback_query(inline.UserSettings.filter(F.action == "lang_but"))
async def change_lang_callback(call: CallbackQuery, callback_data: inline.UserSettings):
    await user_settings.change_lang(call.from_user.id)

    await call.message.edit_reply_markup(
        reply_markup=(await inline.get_user_settings_kb(
            call.message.chat.id,
        ))
    )


@router.callback_query(inline.UserSettings.filter(F.action == "notif_but"))
async def change_notif_callback(call: CallbackQuery, callback_data: inline.UserSettings):
    await user_settings.change_notif(call.from_user.id)

    await call.message.edit_reply_markup(
        reply_markup=(await inline.get_user_settings_kb(
            call.message.chat.id,
        ))
    )
