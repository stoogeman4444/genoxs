# WARNING TEST ZONE!!!

import telebot
import config
import os

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=['video'])
def lab(message):
    fileID = message.video.file_id
    print(fileID)
    file_info = bot.get_file(fileID)
    print(file_info)
    downloaded_file = bot.download_file(file_info.file_path)
    print(downloaded_file)
    filename = "video.mp4"
    file = os.path.join(filename)
    with open(file, 'wb') as new_file:
        new_file.write(downloaded_file)
    pass


bot.polling(none_stop=True)
