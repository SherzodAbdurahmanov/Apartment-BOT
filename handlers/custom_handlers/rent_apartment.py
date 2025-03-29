from telebot.types import CallbackQuery, Message

from database.data import Apartment
from loader import bot
from utils.states import RentApartmentState



@bot.callback_query_handler(func=lambda call: call.data == "rent_apartment")
def start_rent_apartment(call: CallbackQuery):
    bot.send_message(call.message.chat.id, "🏙️ В каком городе вы ищете квартиру?")
    bot.set_state(call.from_user.id, RentApartmentState.city, call.message.chat.id)


@bot.message_handler(state=RentApartmentState.city)
def handle_rent_city(message: Message):
    city = message.text.strip()


    apartments = Apartment.select().where(Apartment.city == city)

    if apartments:
        bot.send_message(message.chat.id, f"🏠 Найдено {len(apartments)} квартир(а) в городе {city}:")
        for apt in apartments:
            bot.send_photo(
                message.chat.id,
                apt.photo,
                caption=(
                    f"📍 Адрес: {apt.address}\n"
                    f"📄 Описание: {apt.description}\n"
                    f"💰 Цена: {apt.price} руб./мес\n"
                    f"📞 Контакты: {apt.contact}"
                )
            )
    else:
        bot.send_message(message.chat.id, f"❌ В городе {city} пока нет доступных квартир.")

    bot.delete_state(message.from_user.id, message.chat.id)
