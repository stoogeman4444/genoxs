import os
import config

from core import bot


def cloud_document():
    @bot.message_handler(content_types=['document'])
    def cmd_cloud_document(message):
        bot.reply_to(message, "<b>Document Received</b>", parse_mode='HTML')
        bot.send_chat_action(message.chat.id, 'upload_document')

        # bot.forward_message(config.ADMIN, message.chat.id, message.message_id)

        fileID = message.document.file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)

        filename = message.document.file_name
        file = os.path.join(config.PATH['document'], filename)
        with open(file, 'wb') as new_file:
            new_file.write(downloaded_file)
        pass

        bot.reply_to(message, "<b>Status: </b>Document Saved\n<b>Name: </b>{0}\n<b>Location: </b>{1}".format(filename, file),
                     parse_mode='HTML')

    pass