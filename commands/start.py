from core import bot


def cmd_start():
    @bot.message_handler(commands=['start'])
    def function_start(message):
        bot.send_message(message.chat.id,
                         f"<b>Welcome {message.from_user.first_name}</b> ༼ つ ◕_◕ ༽つ\n" +
                         f"I'm <i>{bot.get_me().first_name}</i> and I serve as cloud server\n" +
                         f"assistant helper for my Genemator master!\n" + "\n" +
                         f"<b>For further information or help, type</b> /help\n",
                         parse_mode='HTML')
        pass
    pass
