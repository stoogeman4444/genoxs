try:
    import telebot
    import config
    import logging
except ImportError as err:
    print(f"Import failed, {err}")
    exit(1)

bot = telebot.TeleBot(config.TOKEN)


def launch():
    logger = telebot.logger

    def logger_mode(mode):
        if mode == 'MIN':
            return logging.INFO
        else:
            return logging.DEBUG
        pass

    telebot.logger.setLevel(logger_mode(config.LOGGER))

    logging.basicConfig(format='[%(asctime)s] %(filename)s:%(lineno)d %(levelname)s - %(message)s',
                        level=logging.INFO,
                        filename='logs/bot.log', datefmt='%d.%m.%Y %H:%M:%S')

    bot.polling(none_stop=True)
    pass
