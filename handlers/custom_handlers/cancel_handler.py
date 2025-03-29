from telebot.types import Message, ReplyKeyboardRemove
from loader import bot

@bot.message_handler(state="*",func=lambda message: message.content_type in ["text", "photo"] and message.text == "❌ Отмена")
def cancel_handler(message: Message):
    bot.send_message(message.chat.id, "🚫 Добавление квартиры отменено!", reply_markup=ReplyKeyboardRemove())
    bot.delete_state(message.from_user.id, message.chat.id)
