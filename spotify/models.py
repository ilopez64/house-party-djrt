from django.db import models
from api.models import Room

# Create your models here.

class SpotifyToken(models.Model):
    user = models.CharField(unique=True, max_length=100)
    created_at = models.DateField(auto_now_add=True)
    refresh_token = models.CharField(max_length=300)
    access_token = models.CharField(max_length=300)
    expires_in = models.DateTimeField()
    token_type = models.CharField(max_length=50)

class Vote(models.Model):
    user = models.CharField(unique=True, max_length=50)
    created_at = models.DateField(auto_now_add=True)
    song_id = models.CharField(max_length=50)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
