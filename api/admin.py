from django.contrib import admin
from . import models 

# Register your models here.
@admin.register(models.Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'genre']