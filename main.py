import subprocess
import os
import time
import yt_dlp

# YouTube to video
def download_video(url):
    ydl_opts = {
        'outtmpl': 'video.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        return info_dict['ext']

# Video to mp3
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
        subprocess.run(ffmpeg_cmd, check=True)
        print("SUCCESS")
    except subprocess.CalledProcessError:
        print("FAIL")

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ")
    video_ext = download_video(video_url)

    time.sleep(3)

    video_file = f"video.{video_ext}"
    convert_video_to_mp3(video_file, "audio.mp3")

    # Move audio to folder
    if not os.path.exists('music'):
        os.makedirs('music')

    destination = "music/audio.mp3"
    source = "audio.mp3"
    try:
        if os.path.exists(destination):
            print("There is already a file there")
        else:
            os.replace(source, destination)
            print(source + " was moved successfully")
            # Rename audio file
            music = input("Name the audio file: ") + ".mp3"
            os.rename(destination, os.path.join("music", music))
            print(f"File renamed to {music}")
    except FileNotFoundError:
        print("Source not found")

    # Remove video
    if os.path.exists(video_file):
        os.remove(video_file)
    else:
        print("Downloaded video file not found")
