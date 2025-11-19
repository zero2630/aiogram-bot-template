from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

from app.services.user_settings import get_user_settings

class UserSettings(CallbackData, prefix="reaction"):
    action: str

async def get_user_settings_kb(user):
    builder = InlineKeyboardBuilder()

    user_settings = await get_user_settings(user)

    if user_settings:
        lang = "Ru" if user_settings.is_ru else "En"
        notif = "Вкл" if user_settings.is_notificate else "Выкл"
        builder.button(text=f"язык: {lang}", callback_data=UserSettings(action="lang_but"))
        builder.button(text=f"уведомления: {notif}", callback_data=UserSettings(action="notif_but"))
        builder.adjust(1, 1)
        return builder.as_markup(resize_keyboard=True) 