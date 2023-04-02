from pytube import YouTube
from sys import argv

link=argv[1]
yt=YouTube(link)

print("Title: ",yt.title)

print("Views:" , yt.views)

yd= yt.streams.get_highest_resolution()

yd.download("C:/Users/murabıt/Desktop/ytDownload")

#in windows you need to type python ytDownloader.py "youtube link"
