from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputMediaAudio
from key import key
from pytube import YouTube
from moviepy.editor import *
from pydub import AudioSegment


API_TOKEN = key
l=3_000_000

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
    sound = AudioSegment.from_mp3(f"{name}.mp3")
    if len(sound)//l>1:
        for i in range(len(sound)//l+2):
            n=i+1
            if i==len(sound)//l+1:
                sound[(i+1)*l::].export(f"Audio{n}.mp3",format="mp3")
            else:
                sound[l*i:l*(i+1)].export(f"Audio{n}.mp3",format="mp3")
        media=[f"Audio{i}.mp3" for i in range(1,n+1)]
    else:
        media="Audio.mp3"
    return media

@dp.message_handler()
async def echo(message: types.Message):
    for i in f(message.text):
        await bot.send_audio(message.from_user.id, open(i,"rb"))



executor.start_polling(dp, skip_updates=True)
