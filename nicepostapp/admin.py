from django.contrib import admin
from . import models

admin.site.register(models.Post)
admin.site.register(models.Comments)
admin.site.register(models.Imgs)
admin.site.register(models.GIF)
