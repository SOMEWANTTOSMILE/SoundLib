from django.views import View
from django.shortcuts import render, get_object_or_404, HttpResponse
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from music.serializers import (AddSongPlayListSerializer, MyPlayListSerializer,
                               SongInPlayListSerializer, AddFavoriteSongSerializer, AddFavoriteAlbumSerializer,
                               AddFavoriteArtistSerializer)
from music.models import PlaylistSong, PlayList, Album, Song, Artist, Category
from music.forms import PlayListForm


class AddSongPlaylistView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AddSongPlayListSerializer

    def post(self, request):
        serializer = AddSongPlayListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})


class MyPlayListView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MyPlayListSerializer

    def get(self, request):
        user = request.user
        queryset = PlayList.objects.filter(user=user)
        serializer = MyPlayListSerializer(queryset, many=True)
        return Response(serializer.data)


class SongInPlayListView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SongInPlayListSerializer

    def post(self, request):
        # playlists = PlayList.objects.filter(user=request.user)
        playlist_id = request.data['playlist_id']
        queryset = PlaylistSong.objects.filter(playlist_id=playlist_id)
        serializer = SongInPlayListSerializer(queryset, many=True)
        return Response(serializer.data)


class CreatePlayListView(View):
    def post(self, request):
        form = PlayListForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.save()
            return HttpResponse(f'good')
        else:
            return HttpResponse(f'bad')

    def get(self, request):
        form = PlayListForm()
        return render(request, "create_playlist.html", {"form": form})


class AlbumDetailView(View):
    def get(self, request, album_id):
        album = get_object_or_404(Album, id=album_id)
        song = Song.objects.filter(album_id=album_id)
        return render(request, 'album_detail.html', {'album': album, "song": song})


class PlaylistDetailView(View):
    def get(self, request, playlist_id):
        playlist = get_object_or_404(PlayList, id=playlist_id)
        playlist_song = PlaylistSong.objects.filter(playlist_id=playlist.id)
        return render(request, "playlist_detail.html", {"playlist": playlist,
                                                        "song": playlist_song})


class SongDetailView(View):
    def get(self, request, song_id):
        song = get_object_or_404(Song, id=song_id)
        return render(request, "song_detail.html", {"song": song})


class ArtistDetailView(View):
    def get(self, request, artist_id):
        artist = get_object_or_404(Artist, id=artist_id)
        album = Album.objects.filter(artist_id=artist_id)
        return render(request, "artist_detail.html", {"artist": artist, "album": album})


class AllCategoryView(View):
    def get(self, request):
        category = Category.objects.all()
        return render(request, "all_category.html", {"category": category})


class CategorySongView(View):
    def get(self, request, category_id):
        song = Song.objects.filter(category_id=category_id)
        return render(request, "category_song.html", {"song": song})


class AddFavoriteSongView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AddFavoriteSongSerializer

    def post(self, request):
        serializer = AddFavoriteSongSerializer(data=request.data,
                                               context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})


class AddFavoriteAlbumView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AddFavoriteAlbumSerializer

    def post(self, request):
        serializer = AddFavoriteAlbumSerializer(data=request.data,
                                                context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})


class AddFavoriteArtistView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AddFavoriteArtistSerializer

    def post(self, request):
        serializer = AddFavoriteArtistSerializer(data=request.data,
                                                 context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})


class AllAlbumView(View):

    def get(self, request):

        search_query = request.GET.get('search', '')

        if search_query:
            album = Album.objects.filter(title__icontains=search_query)
        else:
            album = Album.objects.all()

        return render(request, "all_album.html", {'album': album})


class AllSongView(View):

    def get(self, request):
        search_query = request.GET.get('search', '')

        if search_query:
            song = Song.objects.filter(title__icontains=search_query)
        else:
            song = Song.objects.all()

        return render(request, 'all_song.html', {'song': song})


class AllArtistView(View):

    def get(self, request):
        search_query = request.GET.get('search', '')

        if search_query:
            artist = Artist.objects.filter(name__icontains=search_query)
        else:
            artist = Artist.objects.all()

        return render(request, 'all-artist.html', {'artist': artist})
