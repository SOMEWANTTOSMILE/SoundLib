from rest_framework import serializers
from music.models import PlayList, PlaylistSong, Album, Song, UserFavoriteSong, UserFavoriteAlbum, UserFavoriteArtist
from datetime import datetime, timedelta


class AddSongPlayListSerializer(serializers.Serializer):
    playlist_id = serializers.IntegerField()
    song_id = serializers.IntegerField()

    def create(self, validated_data):
        return PlaylistSong.objects.create(**validated_data)


class MyPlayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayList
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title', 'artist')


class SongInPlayListSerializer(serializers.Serializer):

    playlist_id = serializers.IntegerField()

    class Meta:
        model = PlaylistSong
        fields = '__all__'


class AddFavoriteSongSerializer(serializers.Serializer):

    song_id = serializers.IntegerField()

    def create(self, validated_data):
        user = self.context["request"].user
        user.save()
        return UserFavoriteSong.objects.create(**validated_data, user=user)


class AddFavoriteAlbumSerializer(serializers.Serializer):

    album_id = serializers.IntegerField()

    def create(self, validated_data):
        user = self.context["request"].user
        user.save()
        return UserFavoriteAlbum.objects.create(**validated_data, user=user)


class AddFavoriteArtistSerializer(serializers.Serializer):

    artist_id = serializers.IntegerField()

    def create(self, validated_data):
        user = self.context["request"].user
        user.save()
        return UserFavoriteArtist.objects.create(**validated_data, user=user)
