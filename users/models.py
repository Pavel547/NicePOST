from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(default="profile_imgs/default.png", upload_to="profile_imgs/")
    
    def __str__(self):
        return f"{self.user.username} profile"
