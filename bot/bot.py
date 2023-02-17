import telebot

from parser.parser import parse

token = ''

bot = telebot.TeleBot(token)

# projects
url = 'https://profile-psi-three.vercel.app/'


@bot.message_handler(commands=['projects'])
def get_projects(message):
    global url
    titles = parse(url)
    bot.send_message(message.chat.id, titles)


# greet


@bot.message_handler(commands=['hello'])
def greet(message):
    bot.send_message(message.chat.id, 'hello, {}'.format(
        message.from_user.first_name))


print('bot is working...')
bot.infinity_polling()
