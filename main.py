import subprocess
import os
import time
import yt_dlp


#Youtube to video
def download_video(url):
    ydl_opts = {
        'outtmpl': 'video.%(ext)s',  # Filename template
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ")
    download_video(video_url)

time.sleep(3)




#Video to mp3
def convert_video_to_mp3(input_file, output_file):
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file,
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", "192k",
        "-ar", "44100",
        "-y",
        output_file
    ]

    try:
        subprocess.run(ffmpeg_cmd, check = True)
        print("SUCCESS")
    except subprocess.CalledProcessError as e:
        print("FAIL")

convert_video_to_mp3("video.webm", "audio.mp3")

#move audio to folder
destination = "music/audio.mp3"
source = "audio.mp3"
try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source +" was moved successfully")
        #rename audio file
        music = input("Name the audio file: ") + ".mp3"
        os.rename(destination, os.path.join("music", music))
        print(f"File renamed to {music}")
except FileNotFoundError:
    print("source not found")

os.remove("video.webm")

