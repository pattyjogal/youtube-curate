from django.db import models
from django.contrib.auth.models import User

class VideoRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField()
    video = models.ForeignKey('Video', on_delete=models.CASCADE, related_name='ratings')

class Video(models.Model):
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()

    def add_rating(self, user, rating):
        return VideoRating.objects.create(user=user, rating=rating, video=self.pk)
