from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Playlist(models.Model):
    songs = models.TextField(default='TunesBeanie Song List')
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING,default='')
    title = models.CharField(max_length=200)
    link = models.TextField(default='TunesBeanie Song Link')
    image = models.TextField(default='tbeanie.jpg')
    class Meta:
        verbose_name_plural = 'playlists'
    def __str__(self):
        return self.title
 
class PlaylistAdmin(admin.ModelAdmin):
    pass

admin.site.register(Playlist, PlaylistAdmin)

class Profile(models.Model):
    avatar = models.TextField(default='tbeanie.jpg')
    date_modified = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING,default='')
    aboutme = models.TextField(default='TunesBeanie About Me')
    class Meta:
        verbose_name_plural = 'profiles'
    def __str__(self):
        return "Profile for " + self.owner
 
class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)


class Comment(models.Model):
    playlist = models.ForeignKey(Playlist,on_delete=models.DO_NOTHING)
    text = models.TextField(default='Pls enter data')
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,default='')
    class Meta:
        verbose_name_plural = 'comments'
    def __str__(self):
        return self.text[:30] + "... from " + self.author  
 
class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comment, CommentAdmin)