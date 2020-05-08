from pytube import YouTube
# Link of video
yt = YouTube("")
yt = yt.get('mp4', '720p')
# Folder for save video
yt.download('')