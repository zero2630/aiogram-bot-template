from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class UserSettings(CallbackData, prefix="reaction"):
    action: str

def get_user_settings_kb(user):
    builder = InlineKeyboardBuilder()
    lang = "ru"
    notif = "true"
    # lang = "ru" if lang == "en" else "en"
    # notif = not notif

    builder.button(text=f"язык: {lang}", callback_data=UserSettings(action="lang_but"))
    builder.button(text=f"уведомления: {notif}", callback_data=UserSettings(action="notif_but"))
    builder.adjust(1, 1)
    return builder.as_markup(resize_keyboard=True) 