from telebot.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from database.data import Apartment
from loader import bot

@bot.callback_query_handler(func=lambda call: call.data == "my_apartments")
def show_my_apartments(call: CallbackQuery):
    user_id = call.from_user.id
    apartments = Apartment.select().where(Apartment.owner_id== user_id)

    if not apartments:
        bot.send_message(call.message.chat.id, "😔 У вас пока нет объявлений.")
        return

    for apt in apartments:
        bot.send_photo(
            call.message.chat.id,
            apt.photo,
            caption=(
                f"🏙️ Город: {apt.city}\n"
                f"📍 Адрес: {apt.address}\n"
                f"📄 Описание: {apt.description}\n"
                f"💰 Цена: {apt.price} руб./мес\n"
                f"📞 Контакты: {apt.contact}"
            ),
            reply_markup=get_apartment_buttons(apt.id)
        )

def get_apartment_buttons(apartment_id):
    keyboard = InlineKeyboardMarkup()
    keyboard.row(
        InlineKeyboardButton("❌ Удалить", callback_data=f"delete_{apartment_id}")
    )
    return keyboard
