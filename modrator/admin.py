from django.contrib import admin
from .models import Category, VideoType, Series, VideoItem, Movie, SiteSettings

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'createdDate', 'trailer_url']

# سجل بقية الموديلات لو محتاجها
admin.site.register(Category)
admin.site.register(VideoType)
admin.site.register(VideoItem)
admin.site.register(Movie)
admin.site.register(SiteSettings)