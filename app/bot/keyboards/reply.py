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
        ],
        resize_keyboard=True,
    )

    return menu


def get_admin_menu():
    menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='статистика'),
                KeyboardButton(text='рассылка'),
            ],
            [
                KeyboardButton(text='пользователи'),
                KeyboardButton(text='выйти'),
            ],
        ],
        resize_keyboard=True,
    )
    
    return menu