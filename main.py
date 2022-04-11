from email import message
import telebot
token = '5233084458:AAE79zJ8kI3Fx7nNmGkpTHI6pyRE-FcyGkI'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    mes = f'hello, {message.from_user.first_name}'
    bot.send_message(message.chat.id, mes)


bot.polling(non_stop=True, interval=0)
