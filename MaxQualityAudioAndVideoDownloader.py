from pytube import YouTube
import os

def combine_audio(vidname, audname, outname, fps=25):    
    import moviepy.editor as mpe
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname,fps=fps)
    print(f">>>>> Video Merge completed {url} ")
    os.remove(vidname)
    os.remove(audname)

def download_task(url):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(file_extension='mp4').order_by("resolution").desc().first().download(output_path="video")
        print(f">>>>> video download completed {url} ")
        audio = yt.streams.filter(only_audio=True).order_by("abr").desc().first().download(output_path="video")
        print(f">>>>> audio download completed {url} ")
        filePath, ext = os.path.splitext(video)
        outfile = filePath + '_final'+ext
        combine_audio(video, audio, outfile)
    except Exception:
        with open("err_link.txt", "w+") as f:
            f.write(url)
       
with open("links.txt", "r") as f:
    l = [tmp for tmp in f]
    for u in l:
        download_task(u)