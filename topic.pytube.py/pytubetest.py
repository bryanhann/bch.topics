# pip install pytube
from pytube import YouTube
#A='https://www.youtube.com/watch?v=R6Xye0ogJ5I'
#YouTube(A
#).streams. get_highest_resolution() . download()

#
YouTube('https://youtu.be/9bZkp7q19f0').streams.get_highest_resolution().download()

yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
(yt.streams\
  .filter(progressive=True, file_extension='mp4')\
 .order_by('resolution')[-1]\
 .download(
)
)
