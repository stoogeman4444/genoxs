import telebot
import config
import logging

bot = telebot.TeleBot(config.TOKEN)


def launch():
    # Importing Telebot's Logs
    logger = telebot.logger
    telebot.logger.setLevel(logging.DEBUG)  # Outputs debug messages to console.

    # Setting up logger
    logging.basicConfig(format='[%(asctime)s] %(filename)s:%(lineno)d %(levelname)s - %(message)s',
                        level=logging.INFO,
                        filename='logs/bot.log', datefmt='%d.%m.%Y %H:%M:%S')
    pass

    # Starting bot polling
    bot.polling(none_stop=True)
