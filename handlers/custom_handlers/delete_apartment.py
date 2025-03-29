from telebot.types import CallbackQuery
from database.data import Apartment
from loader import bot


@bot.callback_query_handler(func=lambda call: call.data.startswith("delete_"))
def delete_apartment(call: CallbackQuery):
    apartment_id = int(call.data.split("_")[1])

    # Удаляем запись из базы данных
    apartment = Apartment.get_or_none(Apartment.id == apartment_id)
    if apartment:
        apartment.delete_instance()
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.answer_callback_query(call.id, "Объявление удалено.")
    else:
        bot.answer_callback_query(call.id, "Ошибка: объявление не найдено.")
