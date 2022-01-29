from django.urls import path
from . import views 

app_name = "api"

urlpatterns = [
     

    path('rest/generics/playlist/', views.PlaylistListView.as_view(), name='playlist_generics'),
    path('rest/playlist/', views.ListPlaylistAPIView.as_view(), name='playlist_list'),
    # path('rest/playlist/view/<int:pk>/', views.DetailPlaylistAPIView.as_view(), name='view_playlistlist'),
     
    path("rest/playlist/create/", views.CreatePlaylistView.as_view(),name="playlist_create"),
    path("rest/playlist/update/<int:pk>/",views.UpdatePlaylistView.as_view(),name="update_playlist"),
    path("rest/playlist/delete/<int:pk>/",views.DeletePlaylistView.as_view(),name="delete_playlist")




]