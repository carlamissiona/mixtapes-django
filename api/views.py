from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .models import *
from api.api_serializers import *
from rest_framework.generics import ListAPIView
#from rest_framework.generics import DetailAPIView
from rest_framework.generics import CreateAPIView 
from rest_framework.generics import DestroyAPIView 
from rest_framework.generics import UpdateAPIView
 
# Create your views here.


 
class PlaylistListView(generic.ListView):
    model = Playlist
    #context_object_name = 'tunes_list'   # your own name for the list as a template variable
    playlist = Playlist.objects.all() # Get 5 books containing the title war
    count = playlist.count()
    template_name = 'api/playlist/list.html'

class ListPlaylistAPIView(ListAPIView):
    """This endpoint allows for creation of a Playlist"""
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

# class ListSinglePlaylistAPIView(DetailAPIView):
#     """This endpoint allows for creation of a Playlist"""
#     queryset = Playlist.objects.all()
#     serializer_class = PlaylistSerializer

class CreatePlaylistView(CreateAPIView):
    """This endpoint allows for creation of a Playlist"""
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class UpdatePlaylistView(UpdateAPIView):
    """This endpoint allows for updating a specific Playlist by passing in the id of the playlist to update"""
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class DeletePlaylistView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Playlist from the database"""
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

# class DetailPlaylistAPIView(DetailAPIView):
#     """This endpoint allows for deletion of a specific Playlist from the database"""
#     queryset = Playlist.objects.all()
#     serializer_class = PlaylistSerializer

 

# class PlaylistDetailApiView(APIView):
#     # add permission to check if user is authenticated
#     permission_classes = [permissions.IsAuthenticated]

#     def get_object(self, playlist_id, user_id): 
#         try:
#             return Playlist.objects.get(id=playlist_id, owner = user_id)
#         except Playlist.DoesNotExist:
#             return None

#     # 3. Retrieve
#     def get(self, request, idpl, *args, **kwargs):
#         '''
#         Retrieves the Playlist with given playlist_id
#         '''
#         this_playlist = self.get_object(idpl, request.user.id)
#         if not this_playlist:
#             return Response(
#                 {"res": "Object with playlist id does not exists"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         serializer = PlaylistSerializer(this_playlist)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # 4. Update
#     def put(self, request, idpl, *args, **kwargs):
#         '''
#         Updates the playlist item with given playlist_id if exists
#         '''
#         this_playlist = self.get_object(idpl, request.user.id)
#         if not this_playlist:
#             return Response(
#                 {"res": "Object with playlist id does not exists"}, 
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         data = {
#             'task': request.data.get('task'), 
#             'completed': request.data.get('completed'), 
#             'user': request.user.id
#         }
#         serializer = PlaylistSerializer(instance = this_playlist, data=data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # 5. Delete
#     def delete(self, request, idpl, *args, **kwargs):
#         '''
#         Deletes the playlist item with given playlist_id if exists
#         '''
#         this_playlist = self.get_object(playlist_id, request.user.id)
#         if not this_playlist:
#             return Response(
#                 {"res": "Object with playlist id does not exists"}, 
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         this_playlist.delete()
#         return Response(
#             {"res": "Object deleted!"},
#             status=status.HTTP_200_OK
#         )