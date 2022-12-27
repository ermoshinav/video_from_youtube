from pytube import YouTube
from pytube import Playlist

# ссылка на загружаемое видео
playlist = Playlist("https://www.youtube.com/playlist?list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6")
 
  
for url in playlist.video_urls:
    print(url)
    
print(f"Загрузка плейлиста: {playlist.title}")
for video in playlist.videos:
    video.streams.first().download()
    print(f"Видео {video.title} загружено")