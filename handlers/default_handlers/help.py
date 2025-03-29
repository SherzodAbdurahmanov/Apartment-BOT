from telebot.types import Message
from loader import bot

@bot.message_handler(commands=["help"])
def bot_help(message: Message):
    text = (
        "🤖 *Команды бота:*\n\n"
        "🏠 /start - Начать работу с ботом\n"
        "📋 /help - Справка по командам\n"
        "🏡 Сдать квартиру - Добавить новое объявление\n"
        "🔍 Снять квартиру - Найти доступные квартиры\n"
        "📜 Мои объявления - Посмотреть или удалить свои объявления\n"
        "❌ Отмена - Прервать процесс добавления квартиры"
    )
    bot.reply_to(message, text, parse_mode="Markdown")
