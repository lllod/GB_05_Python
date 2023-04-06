import telebot
from dotenv import load_dotenv
import os
import wikipedia

load_dotenv()
bot_token = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(bot_token)
wikipedia.set_lang('ru')


def get_wiki(key_words):
    try:
        wikimas = wikipedia.page(key_words).content[:1000].split('.')[:-1]
        return '.'.join(i for i in wikimas if '==' not in i and len(i.strip()) > 3)
    except Exception as e:
        return 'В Wikipedia нет информации об этом'


@bot.message_handler(commands=['start'])
def start(message, res=False):
    markup = telebot.types.ReplyKeyboardMarkup(True)
    markup.row('Погнали', 'Преисполниться')
    bot.send_message(message.chat.id, 'Здарова, бродяга!', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def handle_if(message):
    if 'Погнали' in message.text.strip():
        bot.send_message(message.chat.id, 'Нажми на "Преисполниться" для получения доступа к тайнам мироздания!')
    if 'Преисполниться' in message.text.strip():
        bot_text = bot.send_message(message.chat.id, 'Введи запрос и получи доступ к тайнам мироздания!')
        bot.register_next_step_handler(bot_text, handle_ask)


@bot.message_handler(content_types=['text'])
def handle_ask(message):
    bot.send_message(message.chat.id, f'Ты хочешь обкашлять следующий, значит-с, запросик: {message.text}')
    bot.send_message(message.chat.id, get_wiki(message.text))


bot.polling(none_stop=True, interval=0)
