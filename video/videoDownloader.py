import yt_dlp as youtube
from .utils import duration


def video_info(url: str):

    ydl_opts = {
        'quiet': True,  
        'extract_flat': True,
        'force_generic_extractor': True,  
        'no_warnings': True,  
        'noplaylist': True,  
        'extractor_args': {
            'youtube': ['--no-check-certificate']
        }
    }
    
    with youtube.YoutubeDL(ydl_opts) as yt:
        info = yt.extract_info(url, download=False)
   
    info = {
        "title": info.get("title", None),
        "thumbnail": info.get("thumbnail", None),
        "views": f"{info.get("view_count", None):,}",
        "likes": f"{info.get("like_count", None):,}",
        "length": duration(info.get("duration", None)),
        "upload_date": info.get("upload_date", None),
        "author": info.get("uploader", None),
        "url": url,
    }

    return info

def download_video(url: str):

    ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
            "outtmpl": "%(title)s.%(ext)s",
    }

    with youtube.YoutubeDL(ydl_opts) as yt:
        yt.download([url])

    return True

    
    
