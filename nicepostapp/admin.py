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

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comments, CommentsAdmin)
admin.site.register(models.ImgOrVideo)
