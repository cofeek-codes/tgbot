from email import message
import telebot


def main():

    token = '5233084458:AAE79zJ8kI3Fx7nNmGkpTHI6pyRE-FcyGkI'
    bot = telebot.TeleBot(token)

    bot.polling(non_stop=True, interval=0)


if __name__ == "__main__":
    main()
