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
        
class GIFForm(forms.ModelForm):
    class Meta:
        model = models.GIF
        fields = ["post_gif"]
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comments
        fields = ["comment_text"]
