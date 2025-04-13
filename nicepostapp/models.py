from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(verbose_name="post title", max_length=150)
    content = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='title')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Imgs(models.Model):
    imgs = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="imgs")
    post_imgs = models.ImageField(upload_to="imgs/", blank=True)

    def __str__(self):
        return f"Img for {self.imgs.title}"

class GIF(models.Model):
    gif = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="gif")
    post_gif = models.FileField(upload_to='gifs/', blank=True)

    def __str__(self):
        return f"{self.gif.title} GIF"

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    comment_text = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")

    def __str__(self):
        return f"{self.post.title}"
