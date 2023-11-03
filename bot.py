from aiogram import Bot, Dispatcher, executor, types
from key import key
from pytube import YouTube
from moviepy.editor import *


API_TOKEN = key

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def f(link):
    if link[0:4]!="http":
        link="https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUEcmljaw%3D%3D"
    global name
    youtubeObject = YouTube(link)
    youtubeObject.title='Audio'
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    name=youtubeObject.title
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

    video = VideoFileClip(f"{name}.mp4")
    video.audio.write_audiofile(f"{name}.mp3")
    return f"{name}.mp3"

@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_audio(message.from_user.id,audio=open(f(message.text),"rb"))



executor.start_polling(dp, skip_updates=True)
