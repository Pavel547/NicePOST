from django import forms
from . import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ["title", "content"]
        
class ImgForm(forms.ModelForm):
    class Meta:
        model = models.Imgs
        fields = ["post_imgs"]
        
class VideoForm(forms.ModelForm):
    class Meta:
        model = models.Videos
        fields = ["post_video"]
        
class CommentsForm(forms.ModelForm):
    class Meta:
        model = models.Comments
        fields = ["comment_text"]
