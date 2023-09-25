```
    ____                  __         ____        __           _____            __                     
   / __ \____ _____  ____/ /___ _   / __ \____ _/ /_____ _   / ___/__  _______/ /____  ____ ___  _____
  / /_/ / __ `/ __ \/ __  / __ `/  / / / / __ `/ __/ __ `/   \__ \/ / / / ___/ __/ _ \/ __ `__ \/ ___/
 / ____/ /_/ / / / / /_/ / /_/ /  / /_/ / /_/ / /_/ /_/ /   ___/ / /_/ (__  ) /_/  __/ / / / / (__  ) 
/_/    \__,_/_/ /_/\__,_/\__,_/  /_____/\__,_/\__/\__,_/   /____/\__, /____/\__/\___/_/ /_/ /_/____/  
                                                                /____/                                
```
# Music-DL-Oct2023
Download your favorite music from YouTube in .mp3 format using Python

# Requirements:
pafy
```
pip3 install pafy
```
wget
```
pip3 install wget
```
youtube-dl
```
pip3 install youtube-dl
```
moviepy
```
pip3 install moviepy
```
pydub
```
pip3 install pydub
```

# 💾 Patch Feb 2023:
if your YouTube downloader/downloaders are failing:

Go here:

```
/usr/local/lib/python3.10/site-packages/youtube_dl/extractor/youtube.py
```
search for the uploader id array:

old code:
```
'uploader_id': self._search_regex(r'/(?:channel|user)/([^/?&#]+)', owner_profile_url, 'uploader id') if owner_profile_url else None,
```
Replace with
```
'uploader_id': self._search_regex(r'/(?:channel/|user/|@)([^/?&#]+)', owner_profile_url, 'uploader id', default=None),
```
# Disable ['like_count'] & ['dislike_count']
To continue using Pafy, we need to disable the like count, navigate here:
```
/usr/local/lib/python3.10/dist-packages/pafy
```
Use your favorite editor and edit the ```backend_youtube_dl.py``` file, from here, comment out:
```
# self._likes = self._ydl_info['like_count']
# self._dislikes = self._ydl_info['dislike_count']
```

