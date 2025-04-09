from django.db import models
from autoslug import AutoSlugField

class Post(models.Model):
    title = models.CharField(verbose_name="post title", max_length=150)
    content = models.TextField()
    slug = AutoSlugField(populate_from='title')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Imgs(models.Model):
    imgs = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="imgs")
    post_imgs = models.ImageField(upload_to="imgs/", blank=True)

class Videos(models.Model):
    video = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="video")
    post_video = models.FileField(upload_to='videos/', blank=True)

class Comments(models.Model):
    comment = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment")
    comment_text = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    