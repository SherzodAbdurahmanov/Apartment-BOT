from telebot.types import CallbackQuery, Message, ReplyKeyboardRemove
from database.data import Apartment
from keyboards.reply.cancel_button import cancel_button
from loader import bot
from utils.states import AddApartmentState


@bot.callback_query_handler(func=lambda call: call.data == "add_apartment")
def start_add_apartment(call: CallbackQuery):
    bot.send_message(call.message.chat.id, "📸 Пришлите фото квартиры:\n"
                                           "(Пожалуйста, отправьте одно фото квартиры. Пока альбомы не поддерживаются 😊)",
                                            reply_markup=cancel_button())
    bot.set_state(call.from_user.id, AddApartmentState.photo, call.message.chat.id)


@bot.message_handler(content_types=['photo'], state=AddApartmentState.photo)
def handle_photo(message: Message):
    photo_file_id = message.photo[-1].file_id
    bot.send_message(message.chat.id, "🏙️ В каком городе находится квартира?", reply_markup=ReplyKeyboardRemove())
    bot.set_state(message.from_user.id, AddApartmentState.city, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['photo'] = photo_file_id


@bot.message_handler(state=AddApartmentState.city)
def handle_city(message: Message):
    bot.send_message(message.chat.id, "📍 Укажите точный адрес квартиры:")
    bot.set_state(message.from_user.id, AddApartmentState.address, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['city'] = message.text


@bot.message_handler(state=AddApartmentState.address)
def handle_address(message: Message):
    bot.send_message(message.chat.id, "✍️ Напишите описание квартиры:")
    bot.set_state(message.from_user.id, AddApartmentState.description, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['address'] = message.text


@bot.message_handler(state=AddApartmentState.description)
def handle_description(message: Message):
    bot.send_message(message.chat.id, "💰 Укажите цену за месяц в рублях:")
    bot.set_state(message.from_user.id, AddApartmentState.price, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['description'] = message.text


@bot.message_handler(state=AddApartmentState.price)
def handle_price(message: Message):
    bot.send_message(message.chat.id, "📞 Укажите контактный номер или Telegram:")
    bot.set_state(message.from_user.id, AddApartmentState.contact, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['price'] = message.text


@bot.message_handler(state=AddApartmentState.contact)
def handle_contact(message: Message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['contact'] = message.text

        Apartment.create(
            owner_id=message.from_user.id,
            photo=data['photo'],
            city=data['city'],
            address=data['address'],
            description=data['description'],
            price=data['price'],  
            contact=data['contact']
        )

        bot.send_photo(
            message.chat.id,
            data['photo'],
            caption=(
                f"✅ Квартира добавлена!\n\n"
                f"🏙️ Город: {data['city']}\n"
                f"📍 Адрес: {data['address']}\n"
                f"📄 Описание: {data['description']}\n"
                f"💰 Цена: {data['price']} руб./мес\n"
                f"📞 Контакты: {data['contact']}"
            ), reply_markup=ReplyKeyboardRemove()
        )
    bot.delete_state(message.from_user.id, message.chat.id)
