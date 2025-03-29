from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def cancel_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton("❌ Отмена"))
    return markup
