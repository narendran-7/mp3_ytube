from pytube import YouTube
import os

def download_task(url):
    try:
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).order_by("abr").desc().first()
        out_file = audio.download(output_path="songs")
        filePath, ext = os.path.splitext(out_file)
        new_file = filePath + '.mp3'
        if(os.path.exists(new_file)):
            os.remove(new_file)    
        os.rename(out_file, new_file)
        print(f">>>>> Audio Download completed {u}")
    except Exception:
        with open("err_link.txt", "w+") as f:
            f.write(url)
        
with open("links.txt", "r") as f:
    l = [tmp for tmp in f]
    for u in l:
        download_task(u)
        