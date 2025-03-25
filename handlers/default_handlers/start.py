from telebot.types import Message
from loader import bot
from keyboards.inline.start_buttons import get_start_buttons

@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    photo_path = "media/start_photo.jpg"
    welcome_text = (
        f"Привет, {message.from_user.full_name} 👋\n\n"
        "Я бот для поиска и сдачи квартир 🏠\n\n"
        "Выберите, что хотите сделать:"
    )
    with open(photo_path, 'rb') as photo:
        bot.send_photo(
            message.chat.id,
            photo,
            caption=welcome_text,
            reply_markup=get_start_buttons()
        )
