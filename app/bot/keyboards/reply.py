from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(
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
