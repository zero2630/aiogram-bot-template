from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

from app.services.user_settings import get_user_settings

class Default(CallbackData, prefix="default"):
    action: str

class UserSettings(CallbackData, prefix="settings"):
    action: str

class Broadcast(CallbackData, prefix="broadcast"):
    action: str
    text: str


class Paginator(CallbackData, prefix="paginator"):
    action: str
    page: int
    total_pages: int


async def get_user_settings_kb(user):
    kb = InlineKeyboardBuilder()

    user_settings = await get_user_settings(user)

    if user_settings:
        lang = "Ru" if user_settings.is_ru else "En"
        notif = "Вкл" if user_settings.is_notificate else "Выкл"
        kb.button(text=f"язык: {lang}", callback_data=UserSettings(action="lang_but"))
        kb.button(text=f"уведомления: {notif}", callback_data=UserSettings(action="notif_but"))
        kb.adjust(1, 1)
        return kb.as_markup(resize_keyboard=True) 


def get_pagination_kb(
    page: int,
    total_pages: int,
):

    if total_pages < 1:
        total_pages = 1
    if page < 1:
        page = 1
    if page > total_pages:
        page = total_pages

    kb = InlineKeyboardBuilder()

    # Кнопка "Назад"
    if page > 1:
        kb.button(
            text="« Назад",
            callback_data=Paginator(action="prev", page=page-1, total_pages=total_pages)
        )

    # Кнопка с текущей страницей (просто индикатор)
    kb.button(
        text=f"Стр. {page}/{total_pages}",
        callback_data="noop"
    )

    # Кнопка "Вперёд"
    if page < total_pages:
        kb.button(
            text="Вперёд »",
            callback_data=Paginator(action="next", page=page+1, total_pages=total_pages)
        )

    kb.adjust(3)

    return kb.as_markup()

def get_broadcast_confirm_kb(text):
    kb = InlineKeyboardBuilder()

    kb.button(text=f"отправить", callback_data=Broadcast(action="send", text=text))
    kb.button(text=f"отмена", callback_data=Broadcast(action="cancel", text=""))
    kb.adjust(2)
    
    return kb.as_markup(resize_keyboard=True) 


def get_broadcast_received_kb():
    kb = InlineKeyboardBuilder()

    kb.button(text=f"получено ✅", callback_data=Default(action="received"))
    
    return kb.as_markup(resize_keyboard=True) 
