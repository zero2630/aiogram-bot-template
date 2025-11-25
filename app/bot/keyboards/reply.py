from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu():
    menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='профиль'),
                KeyboardButton(text='настройки'),
            ],
            [
                KeyboardButton(text='о боте'),
                KeyboardButton(text='поддержка'),
            ],
            [
                KeyboardButton(text="смотреть страницы")
            ]
        ],
        resize_keyboard=True,
    )

    return menu


def get_admin_menu():
    menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='создать страницу'),
                KeyboardButton(text='рассылка'),
            ],
            [
                KeyboardButton(text='👥 Пользователи'),
                KeyboardButton(text='⬅️ Выйти'),
            ],
        ],
        resize_keyboard=True,
    )
    
    return menu


def get_admin_users_menu():
    menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='📋 Список'),
                KeyboardButton(text='📤 Экспорт'),
            ],
            [
                KeyboardButton(text='🔍 Поиск'),
                KeyboardButton(text='⬅️ Назад'),
            ],
        ],
        resize_keyboard=True,
    )
    
    return menu


def get_cancel_menu():
    menu = ReplyKeyboardMarkup(
        keyboard = [
            [KeyboardButton(text="отмена")]
        ]
    )

    return menu
