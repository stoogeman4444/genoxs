# WARNING TEST ZONE!!!

import telebot
import config
import os
import stagger

bot = telebot.TeleBot(config.TOKEN)


youtube = 'http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?'



@bot.message_handler(content_types=['audio'])
def cmd_cloud_audio(message):
    bot.reply_to(message, "<b>Audio Received</b>", parse_mode='HTML')
    bot.send_chat_action(message.chat.id, 'upload_audio')

    # bot.forward_message(config.ADMIN, message.chat.id, message.message_id)

    fileID = message.audio.file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)

    filename = message.audio.title + " - " + message.audio.performer + ".mp3"
    file = os.path.join(config.PATH['audio'], filename)
    with open(file, 'wb') as new_file:
        new_file.write(downloaded_file)
        mp3 = stagger.read_tag(downloaded_file)
        mp3.title = message.audio.title
        mp3.artist = message.audio.performer
        mp3.picture = message.audio.thumb.file_id
        mp3.write(file)
    print(file)

    bot.reply_to(message, "<b>Status:</b>Audio Saved\n<b>Name:</b>{0}\n<b>Location:</b>{1}".format(filename, config.PATH),
                 parse_mode='HTML')


bot.polling(none_stop=True)
