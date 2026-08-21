from django.shortcuts import render, get_object_or_404
from .models import VideoItem

def videoDetails(request, id):
    video = get_object_or_404(VideoItem, id=id)
    
    # تحويل رابط يوتيوب ليعمل داخل iframe
    embed_url = None
    if video.trailer_url:
        url = video.trailer_url
        if "youtube.com/watch?v=" in url:
            video_id = url.split("watch?v=")[1].split("&")[0]
            embed_url = f"https://www.youtube.com/embed/{video_id}"
        elif "youtu.be/" in url:
            video_id = url.split("youtu.be/")[1].split("?")[0]
            embed_url = f"https://www.youtube.com/embed/{video_id}"
        else:
            embed_url = url

    context = {
        'video': video,
        'embed_url': embed_url,
    }
    # تأكد تماماً أن المسار يشير لـ AdminPanel/videoDetails.html
    return render(request, 'AdminPanel/videoDetails.html', context)