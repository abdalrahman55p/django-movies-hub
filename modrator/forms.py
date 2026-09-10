from django import forms
from .models import Category, VideoType, Series, VideoItem

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
        fields = '__all__'
class VideoItemForm(forms.ModelForm):
    class Meta:
        model = VideoItem
        fields = ['title', 'description', 'poster', 'video_file', 'trailer_url']