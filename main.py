from email import message
import telebot

from parser import parse


token = '5233084458:AAE79zJ8kI3Fx7nNmGkpTHI6pyRE-FcyGkI'
bot = telebot.TeleBot(token)

url = ''


def main():
    global token, bot, url
    parse(url)
    bot.polling(non_stop=True, interval=0)


if __name__ == "__main__":
    main()
