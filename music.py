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
audio.export(mp3_file, format="mp3")

# Clean up the intermediate files
os.remove(audio_file)

print(f"Video converted to {mp3_file}")
