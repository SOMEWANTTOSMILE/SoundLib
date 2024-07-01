from django.db import models
from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file_path = models.FileField(upload_to='courses/')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    lyrics = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class PlayList(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class PlaylistSong(models.Model):
    playlist = models.ForeignKey(PlayList, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)



