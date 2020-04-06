import config

from pytube import YouTube
from time import sleep
from core import bot


def youtube():
    @bot.message_handler(
        regexp="(?:https?:\/\/)?(?:www\.)?youtu\.?be(?:\.com)?\/?.*(?:watch|embed)?(?:.*v=|v\/|\/)([\w\-_]+)\&?")
    def function_youtube(message):
        sleep(1)
        bot.reply_to(message, "<b>Download Started</b>", parse_mode='HTML')
        bot.send_chat_action(message.chat.id, 'upload_video')
        yt = YouTube(message.text)
        yt.streams\
            .filter(adaptive=True, file_extension='mp4')\
            .order_by('resolution')\
            .desc()\
            .first()\
            .download(config.PATH['youtube'])
        filename = config.PATH['youtube'] + '\\' + yt.title
        bot.reply_to(message, "<b>Status: </b>Video Saved\n<b>Name: </b>{0}\n<b>Location: </b>{1}".format(yt.title, filename),
                     parse_mode='HTML')
        sleep(3)
        bot.send_video(message.chat.id, filename)

    pass
