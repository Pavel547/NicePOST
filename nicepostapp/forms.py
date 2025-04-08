from django import forms

from .models import Post, Imgs, Videos

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', ]
        
class ImgsForm(forms.ModelForm):
    class Meta:
        model = Imgs
        fields = ['post_imgs']
        
class VideoForm(forms.ModelForm):
    class Meta:
        model = Videos
        fields = ['post_video']
