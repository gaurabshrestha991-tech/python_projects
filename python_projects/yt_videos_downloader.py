import yt_dlp

url = input("Enter Youtube video URL: ")


options = {
    "format" : "best",
    "outtmpl" : "%(title)s.%(ext)s"
}

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([url])
    
print("Download completed!")