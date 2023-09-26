#     ____                  __         ____        __           _____            __
#    / __ \____ _____  ____/ /___ _   / __ \____ _/ /_____ _   / ___/__  _______/ /____  ____ ___  _____
#   / /_/ / __ `/ __ \/ __  / __ `/  / / / / __ `/ __/ __ `/   \__ \/ / / / ___/ __/ _ \/ __ `__ \/ ___/
#  / ____/ /_/ / / / / /_/ / /_/ /  / /_/ / /_/ / /_/ /_/ /   ___/ / /_/ (__  ) /_/  __/ / / / / (__  )
# /_/    \__,_/_/ /_/\__,_/\__,_/  /_____/\__,_/\__/\__,_/   /____/\__, /____/\__/\___/_/ /_/ /_/____/
#                                                                 /____/
# Written By: Immain
# Date Created: 9/25/2023
# Version: 1.0.0
# Description: Download your favorite music from YouTube using Python

import pafy
import re
import wget
import os
from moviepy.editor import *
from pydub import AudioSegment

def generate_valid_filename(title):
    # Replace invalid characters with underscores
    valid_chars = "-_() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    filename = ''.join(c if c in valid_chars else '_' for c in title)
    return filename

url = input("Add YouTube Link: ")

result = pafy.new(url)

videoTitle = result.title

# Generate a valid filename from the video title
valid_filename = generate_valid_filename(videoTitle)
exp = "^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*"
s = re.findall(exp, url)[0][-1]
thumbnail = f"https://i.ytimg.com/vi/{s}/maxresdefault.jpg"
file = f"{valid_filename}.jpg"
wget.download(thumbnail)
os.rename("maxresdefault.jpg", file)
print(thumbnail)

bestaudio = result.getbestaudio(preftype="m4a")

audio_file = f"{valid_filename}.m4a"
bestaudio.download(filepath=audio_file)

# Convert the downloaded audio to MP3 format
audio = AudioSegment.from_file(audio_file, format="m4a")
mp3_file = f"{valid_filename}.mp3"
audio.export(mp3_file, format="mp3", bitrate="192k")

# Clean up the intermediate files
os.remove(audio_file)

print(f"Video converted to {mp3_file} (192kbps)")
