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
        fields = ['title', 'description', 'seriesPoster', 'seriesVideo']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter series title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter series description'}),
            'seriesPoster': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'seriesVideo': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'video/*'}),
        }






class VideoItemForm(forms.ModelForm):
    title = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter video title',
            'id': 'title',
            'class': 'form-control'
        })
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter video description',
            'id': 'description',
            'class': 'form-control'
        })
    )

    video = forms.FileField(
        widget=forms.ClearableFileInput(attrs={
            'multiple': False,
            'id': 'video',
            'class': 'form-control'
        })
    )

    poster = forms.ImageField(   
        widget=forms.ClearableFileInput(attrs={
            'multiple': False,
            'accept': 'image/*',
            'id': 'poster',
            'class': 'form-control'
        })
    )

    class Meta:
        model = VideoItem
        fields = ['title', 'description', 'video', 'poster', 'itemCategory', 'itemType', 'series']
        labels = {
            'title': 'Video Title',
            'description': 'Description',
            'video': 'Upload Video',
            'poster': 'Upload Poster',
            'itemCategory': 'Category',
            'itemType': 'Video Type',
            'series': 'Series',
        }




 