try:
    from core import bot
except ImportError as err:
    print(f"Import failed, {err}")
    exit(1)


def cmd_error():
    @bot.message_handler(func=lambda message: True, content_types=['text'])
    def function_error(message):
        bot.send_message(message.chat.id,
                         f"<b>Dear {message.from_user.first_name}</b>.\n" +
                         f"I could not understand what command you insert.\n" +
                         f"Currently, I'm underdevelopment and occasion errors might occur!\n" + "\n" +
                         f"<b>Please, for further information or help, type</b> /help\n",
                         parse_mode='HTML')
        pass
    pass
