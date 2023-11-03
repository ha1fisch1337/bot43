from pytube import YouTube
from moviepy.editor import *

def Download(link):
    global name
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    name=youtubeObject.title
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

def m4to3(path):
    video = VideoFileClip(f"{path}.mp4")
    video.audio.write_audiofile(f"{path}.mp3")
Download("https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUEcmljaw%3D%3D")
m4to3(name)