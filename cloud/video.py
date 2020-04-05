import os
import config
import datetime


from core import bot


def cloud_video():
    @bot.message_handler(content_types=['video'])
    def cmd_cloud_video(message):
        bot.reply_to(message, "<b>Video Received</b>", parse_mode='HTML')
        bot.send_chat_action(message.chat.id, 'upload_video')

        # bot.forward_message(config.ADMIN, message.chat.id, message.message_id)

        fileID = message.video.file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)

        date = datetime.datetime.now()
        filename = str(date).replace(":", "-") + "-video.mp4"
        file = os.path.join(config.PATH['video'], filename)
        with open(file, 'wb') as new_file:
            new_file.write(downloaded_file)
        pass

        bot.reply_to(message, "<b>Status:</b>Video Saved\n<b>Name:</b>{0}\nLocation:{1}".format(filename, config.PATH), parse_mode='HTML')
    pass
