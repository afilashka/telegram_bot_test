import telebot
import setting
import zaprosy_vk

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
    bot.send_message(message.from_user.id, name + ', введи пожалуйста id пользователя для которого хотите получить информацию');
    bot.register_next_step_handler(message, get_id);

def get_id(message):
    global vk_id;
    global user_info;
    vk_id = message.text;
    try:
        vk_id = int(message.text) #проверяем, что введен корректно
    except Exception:
        bot.send_message(message.from_user.id, 'вводить надо цифровое значение, попробуй еще раз');
        bot.register_next_step_handler(message, get_id);
    else:
        user_info = zaprosy_vk.get_profiles(vk_id, setting.token_vk_api);
        bot.send_message(message.from_user.id, user_info);
        bot.send_message(message.from_user.id, 'повторить? - напиши да');
        bot.register_next_step_handler(message, get_one_more_id);


def get_one_more_id(message):
    global yes_no;
    yes_no = message.text;
    if yes_no == 'да' or yes_no == 'Да':
        bot.send_message(message.from_user.id, name + ', введи пожалуйста id пользователя для которого хотите получить информацию');
        bot.register_next_step_handler(message, get_id);
    else:
        bot.send_message(message.from_user.id, 'До встречи ' + name + '!');


bot.polling(none_stop=True, interval=0)

