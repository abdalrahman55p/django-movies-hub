from django import forms
from .models import VideoItem, Category, VideoType, Series


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class VideoTypeForm(forms.ModelForm):
    class Meta:
        model = VideoType
        fields = '__all__'

class SeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = ['title', 'description', 'seriesPoster', 'seriesVideo', 'trailer_url']
        labels = {
            'title': 'Series Title',
            'description': 'Description',
            'seriesPoster': 'Upload Series Poster',
            'seriesVideo': 'Upload Series Video File', # اسم الخانة التي ستظهر
            'trailer_url': 'Trailer Link / URL',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter series title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter series description'}),
            'seriesPoster': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'seriesVideo': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'video/*'}),
            'trailer_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
        }

class VideoItem(models.Model):
    # ... بقية الحقول الخاصة بك ...
    trailer_url = models.URLField(blank=True, null=True)

    # أضف هذه الدالة داخل الكلاس
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
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter video title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter video description', 'rows': 4}),
            'video': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'trailer_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://www.youtube.com/embed/XXXXXX'}),
            'poster': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'itemCategory': forms.Select(attrs={'class': 'form-control'}),
            'itemType': forms.Select(attrs={'class': 'form-control'}),
            'series': forms.Select(attrs={'class': 'form-control'}),
        }