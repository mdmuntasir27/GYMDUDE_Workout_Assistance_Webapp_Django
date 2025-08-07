from django.db import models

# Create your models here.
class Workout(models.Model):
    name = models.CharField(max_length=255)
    benefits = models.CharField(max_length=5000)
    instructions = models.CharField(max_length=5000)
    video_link = models.CharField(max_length=255)

    def __str__(self):
        return self.name