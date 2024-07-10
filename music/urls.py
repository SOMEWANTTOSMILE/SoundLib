from django.urls import path
from rest_framework import routers

from music.views import (AddSongPlaylistView, MyPlayListView,
                         SongInPlayListView, CreatePlayListView, AlbumDetailView,
                         PlaylistDetailView, SongDetailView, ArtistDetailView,
                         AllCategoryView, CategorySongView, AddFavoriteSongView,
                         AddFavoriteAlbumView, AddFavoriteArtistView, AllAlbumView,
                         AllSongView, AllArtistView)


urlpatterns = [
    path('playlist-song/', AddSongPlaylistView.as_view(), name="add-playlist-song"),
    path('my-playlist/', MyPlayListView.as_view(), name='my-playlist'),
    path('my-playlist-song/', SongInPlayListView.as_view(), name='my-playlist-song'),
    path('playlist/', CreatePlayListView.as_view(), name='create-playlist'),
    path('album/<int:album_id>', AlbumDetailView.as_view(), name='album-detail'),
    path('playlist/<int:playlist_id>', PlaylistDetailView.as_view(), name='playlist-detail'),
    path('song/<int:song_id>', SongDetailView.as_view(), name='song-detail'),
    path('artist/<int:artist_id>', ArtistDetailView.as_view(), name='artist-detail'),
    path('category/', AllCategoryView.as_view(), name='all-category'),
    path('category/<int:category_id>', CategorySongView.as_view(), name='category-song'),
    path('favorite-song/', AddFavoriteSongView.as_view(), name='add-favorite-song'),
    path('favorite-album/', AddFavoriteAlbumView.as_view(), name='add-favorite-album'),
    path('favorite-artist/', AddFavoriteArtistView.as_view(), name='add-favorite-artist'),
    path('albums/', AllAlbumView.as_view(), name='all-album'),
    path('songs/', AllSongView.as_view(), name='all-song'),
    path('artist/', AllArtistView.as_view(), name='all-artist'),
]

