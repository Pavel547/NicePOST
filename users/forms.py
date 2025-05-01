from django import forms
from .models import Profile
from PIL import Image

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profile_img"]
        
        # def clean_profile_img():
            
