import config

from pytube import YouTube
from core import bot


def cloud_youtube():
    @bot.message_handler(
        regexp="(?:https?:\/\/)?(?:www\.)?youtu\.?be(?:\.com)?\/?.*(?:watch|embed)?(?:.*v=|v\/|\/)([\w\-_]+)\&?")
    def cmd_cloud_youtube(message):
        bot.reply_to(message, "<b>Download Started</b>", parse_mode='HTML')
        bot.send_chat_action(message.chat.id, 'upload_video')
        yt = YouTube(message.text)
        yt.streams\
            .filter(progressive=True, file_extension='mp4')\
            .order_by('resolution')\
            .desc()\
            .first()\
            .download(config.PATH['youtube'])
        filename = config.PATH['youtube'] + '\\' + yt.title
        bot.reply_to(message, "<b>Status: </b>Video Saved\n<b>Name: </b>{0}\n<b>Location: </b>{1}".format(yt.title, filename),
                     parse_mode='HTML')

    pass
