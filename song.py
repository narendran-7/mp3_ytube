from pytube import YouTube
import os

def download_task(url):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path="songs")
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
    except Exception:
        with open("err_link.txt", "w+") as f:
            f.write(url)
        

with open("links.txt", "r") as f:
    l = [tmp for tmp in f]
    for u in l:
        download_task(u)
        print(f">>>>> completed {u}")
        

