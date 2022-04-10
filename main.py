import telebot
token = '5233084458:AAE79zJ8kI3Fx7nNmGkpTHI6pyRE-FcyGkI'
bot = telebot.TeleBot(token)


# messanger

@bot.message_handler(content_types=['text'])
def messanger(message):
    if message.text == 'hello':
        bot.send_message(message.from_user.id, 'hello, friend')
    else:
        bot.send_message(message.from_user.id, 'do i know you?')


bot.polling(non_stop=True, interval=0)
