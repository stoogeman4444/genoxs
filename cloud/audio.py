import os
import config

from core import bot


def cloud_audio():
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
        pass

        bot.reply_to(message, "<b>Status: </b>Audio Saved\n<b>Name: </b>{0}\n<b>Location: </b>{1}".format(filename, file),
                     parse_mode='HTML')

    pass
