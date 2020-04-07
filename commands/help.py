from core import bot
from telebot import util

help_message = util.split_string(open("assets/templates/help.html", "rb").read(), 3000)


def cmd_help():
    @bot.message_handler(commands=['help'])
    def function_help(message):
        bot.send_message(message.chat.id, help_message, parse_mode='HTML')
    pass
