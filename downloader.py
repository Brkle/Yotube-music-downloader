from pytube import YouTube
import os
while True:
    link = input("Enter YT link: ")
    yt = YouTube(link)
    path = "/home/markoangelovski/Downloads/music/"
    mp4 = yt.streams.filter(only_audio=True).first()
    out_file = mp4.download(output_path=path)

    base, ext = os.path.splitext(out_file)
    mp3 = base + '.mp3'
    os.rename(out_file, mp3)
    print ("successfully downloaded:  " + yt.title)
