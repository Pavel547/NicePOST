from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Content", {"fields": ["title", "content"]}),
        ("Author", {"fields": ["author"]}),
        ("Pub date", {"fields": ["created_on"]}),
    ]
    list_display = ["title", "author", "created_on"]

class CommentsAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Content", {"fields": ["post", "comment_text"]}),
        ("Author", {"fields": ["author"]}),
        ("Pub date", {"fields": ["created_on"]}),
    ]
    list_display = ["comment_text", "author", "created_on"]

class ImgsAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Choice post", {"fields": ["imgs"]}),
        ("Adding an image", {"fields": ["post_imgs"]}),
    ]
    list_display = ["imgs", "post_imgs"]

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comments, CommentsAdmin)
admin.site.register(models.Imgs, ImgsAdmin)
admin.site.register(models.GIF)
