from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    poster = models.ImageField(upload_to='posters/')

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100, null=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title




class VideoType(models.Model):
    title = models.CharField(max_length=100, null=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title






class Series(models.Model): 
    
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)  
    createdDate = models.DateTimeField(auto_now_add=True)
    seriesPoster = models.ImageField(upload_to='series_posters/', blank=True, null=True)
    seriesVideo = models.FileField(upload_to='series_videos/', blank=True, null=True)
    video = models.FileField(upload_to='series_videos/', blank=True, null=True)

    def __str__(self):
        return self.title




# Create your models here.
class VideoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video = models.FileField(upload_to='videos/')
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    itemCategory = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    itemType = models.ForeignKey(VideoType, on_delete=models.SET_NULL, null=True)
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True, blank=True)


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