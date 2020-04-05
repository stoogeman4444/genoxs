try:
    from core import bot
except ImportError as err:
    print(f"Import failed, {err}")
    exit(1)


def cmd_error():
    @bot.message_handler(commands=['start'])
    def function_error(message):
        bot.send_message(message.chat.id,
                         f"<b>Welcome {message.from_user.first_name}</b>\n" +
                         f"I'm <i>{bot.get_me().first_name}</i> and I serve as cloud server\n" +
                         f"machine helper for my Genemator master!\n" + "\n" +
                         f"<b>For further information or help, type</b> /help\n",
                         parse_mode='HTML')
        pass
    pass
