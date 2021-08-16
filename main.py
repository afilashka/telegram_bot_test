import telebot
import setting

bot = telebot.TeleBot(setting.TOKEN)
name = '';
surname = '';
vk_id = 0;

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg');

def get_name(message): #получаем имя, запрашиваем id
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, name + ', введите пожалуйста id пользователя для которого хотите получить информацию');
    bot.register_next_step_handler(message, get_id);

def get_id(message):
    global vk_id;
    vk_id = message.text;
    try:
        vk_id = int(message.text) #проверяем, что введен корректно
    except Exception:
        bot.send_message(message.from_user.id, 'вводить надо цифровое значение, попробуй еще раз ввести, ты сможешь!');
        bot.register_next_step_handler(message, get_id);
    else:
        bot.send_message(message.from_user.id, 'вы запрашиваете данные об id = ' + str(vk_id) + '?')



bot.polling(none_stop=True, interval=0)

