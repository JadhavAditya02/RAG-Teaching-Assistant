import os
import subprocess

files = os.listdir("videos")
for file in files:
    tutorial_number = file.split("Tutorial #")[-1].split("_")[0]
    title = file.split("SSYouTube.online_")[1].split("  Sigma")[0].strip()
    print(tutorial_number, title)
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{tutorial_number}_{title}.mp3"])