from django.contrib import admin
from .models import Series

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'trailer_url']  # تم حذف createdDate مؤقتاً