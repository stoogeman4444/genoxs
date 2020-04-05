from core import bot


def cmd_start():
    @bot.message_handler(commands=['start'])
    def cmdStart(message):
        bot.send_message(message.chat.id,
                         "Welcome {}!".format(message.messa))
    pass
