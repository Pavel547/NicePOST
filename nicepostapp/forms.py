from django import forms
from . import models
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ["title", "content"]
        
    def clean_title(self):
        data = self.cleaned_data["title"]
        if len(data) > 150:
            raise ValidationError("You have exceeded the 150 character limit.")
        if len(data) < 5:
            raise ValidationError("Minimum 5 characters required")
        return data
        
class ImgOrVideoForm(forms.ModelForm):
    class Meta:
        model = models.ImgOrVideo
        fields = ["files"]
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comments
        fields = ["comment_text"]
        
    def clean_comment_text(self):
        data = self.cleaned_data["comment_text"]
        if len(data) < 0:
            raise ValidationError("Comment field is empty")
        return data
