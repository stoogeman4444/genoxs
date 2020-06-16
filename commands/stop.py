from time import sleep
from core import bot


def cmd_stop():
    @bot.message_handler(commands=['stop'])
    def function_stop(message):
        bot.send_message(message.chat.id,
                         f"<b>ATTENTION!!! </b> ༼ つ ◕_◕ ༽つ\n" +
                         f"{message.from_user.first_name}, I'm terminating myself!\n" +
                         f"Get ready...\n" + "\n" +
                         f"<b>For further information or help, type</b> /help\n",
                         parse_mode='HTML')

        sleep(1)
        bot.send_message(message.chat.id, '<b>3...</b>', parse_mode='HTML')

        sleep(1)
        bot.send_message(message.chat.id, '<b>2...</b>', parse_mode='HTML')

        sleep(1)
        bot.send_message(message.chat.id, '<b>1...</b>', parse_mode='HTML')

        exit(1)
        exit(1)
        pass

    pass
