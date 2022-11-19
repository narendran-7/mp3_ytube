from pytube import YouTube
import os

def download_task(url):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution().download(output_path="video")
        print(f">>>>> Video Download completed {url} ")
    except Exception:
        with open("err_link.txt", "w+") as f:
            f.write(url)
       
with open("links.txt", "r") as f:
    l = [tmp for tmp in f]
    for u in l:
        download_task(u)
        