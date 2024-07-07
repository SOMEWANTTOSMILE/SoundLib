from django.contrib import admin
from music.models import Album, Song, PlayList, PlaylistSong, Artist, Category


admin.site.register(Album)
admin.site.register(Song)
admin.site.register(PlayList)
admin.site.register(PlaylistSong)
admin.site.register(Artist)
admin.site.register(Category)

# Register your models here.
