# from aiogram.utils.keyboard import InlineKeyboardBuilder
# from aiogram.filters.callback_data import CallbackData


# class UserSettings(CallbackData, prefix="reaction"):
#     action: str

# def get_user_settings_kb(user):
#     builder = InlineKeyboardBuilder()
#     builder.button(text="ответить", callback_data=AnswAdmin(action="answ_admin"))
#     return builder.as_markup(resize_keyboard=True)