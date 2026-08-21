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
        fields = ['title', 'description', 'seriesPoster', 'trailer_url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter series title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter series description'}),
            'seriesPoster': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'trailer_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://www.youtube.com/embed/XXXXXX'}),
        }


class VideoItemForm(forms.ModelForm):
    class Meta:
        model = VideoItem
        fields = ['title', 'description', 'video', 'trailer_url', 'poster', 'itemCategory', 'itemType', 'series']
        labels = {
            'title': 'Video Title',
            'description': 'Description',
            'video': 'Upload Video File',
            'trailer_url': 'APK / Trailer Link',
            'poster': 'Upload Poster',
            'itemCategory': 'Category',
            'itemType': 'Video Type',
            'series': 'Series',
        }
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