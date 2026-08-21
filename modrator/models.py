from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class VideoType(models.Model):
    title = models.CharField(max_length=100)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Series(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    seriesPoster = models.ImageField(upload_to='series_posters/', blank=True, null=True)
    seriesVideo = models.FileField(upload_to='series_videos/', blank=True, null=True) # أضف هذا السطر
    trailer_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title

class VideoItem(models.Model):
    # ... حقولك الحالية (title, description, video, trailer_url, etc.) ...

    def get_embed_url(self):
        if not self.trailer_url:
            return None
        url = self.trailer_url
        if 'youtu.be/' in url:
            video_id = url.split('youtu.be/')[1].split('?')[0]
            return f"https://www.youtube.com/embed/{video_id}"
        elif 'watch?v=' in url:
            video_id = url.split('watch?v=')[1].split('&')[0]
            return f"https://www.youtube.com/embed/{video_id}"
        elif 'embed/' in url:
            return url
        return url


# الموديل المطلوب لإصلاح ImportError
class Movie(models.Model):
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    video_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, default="موقعي")
    site_url = models.URLField(blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    logo = models.ImageField(upload_to='settings/', blank=True, null=True)
    dark_mode = models.CharField(
        max_length=10,
        choices=[('on', 'تشغيل'), ('off', 'إيقاف')],
        default='off'
    )
    site_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return "إعدادات الموقع"

    class Meta:
        verbose_name = "إعداد الموقع"
        verbose_name_plural = "إعدادات الموقع"