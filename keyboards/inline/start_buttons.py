from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_start_buttons():
    keyboard = InlineKeyboardMarkup()
    keyboard.row(
        InlineKeyboardButton("📢 Сдать квартиру", callback_data="add_apartment"),
        InlineKeyboardButton("🔍 Снять квартиру", callback_data="rent_apartment"),
    )
    keyboard.row(
        InlineKeyboardButton("🏠 Мои объявления", callback_data="my_apartments")
    )
    return keyboard

