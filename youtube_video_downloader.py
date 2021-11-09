"""#YouTube Video Downloader
Pafy - download YouTube content and retrieve metadata

youtube_dl - optionally depends on youtube-dl
"""

pip install pafy

pip install youtube_dl

import pafy

# url of video
url = "https://www.youtube.com/watch?v=3ZXQRuf24Oc"

#Retrieve metadata
# instant created
video = pafy.new(url)

# print title
print(video.title)
  
# print rating
print(video.rating)
  
# print viewcount
print(video.viewcount)

# getting thumb image
print(video.thumb)
  
# print author & video length
print(video.author, video.length)
  
# print duration, likes, dislikes & description
#print(video.duration, video.likes, video.dislikes, video.description)

#Download best resolution video regardless of extension 
streams = video.streams
for i in streams:
    print(i)
      
# get best resolution regardless of format
best = video.getbest()
  
print(best.resolution, best.extension)
  
# Download the video
best.download()

#Download a specific format audio.

audiostreams = video.audiostreams
for i in audiostreams:
    print(i.bitrate, i.extension, i.get_filesize())
  
audiostreams[3].download()


#Download the bestaudio
bestaudio = video.getbestaudio()
bestaudio.download()
