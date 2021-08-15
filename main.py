import telebot
import settings

bot = telebot.TeleBot(settings.TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    msg = message.text + ' 123'
    bot.send_message(message.from_user.id, msg)


bot.polling(none_stop=True, interval=0)