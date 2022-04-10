from email import message
import telebot
token = '5233084458:AAE79zJ8kI3Fx7nNmGkpTHI6pyRE-FcyGkI'
bot = telebot.TeleBot(token)


# messanger

@bot.message_handler(content_types=['text'])
def messanger(message):
    if message.text == 'hello':
        bot.send_message(message.from_user.id, 'hello, friend')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'type \'hello\'')
    else:
        bot.send_message(message.from_user.id, 'type \'/help\'')


bot.polling(non_stop=True, interval=0)
