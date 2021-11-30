from django.db import models
from datetime import timedelta

class Participant(models.Model):
    name = models.CharField(max_length=100)
    workout1_time = models.DurationField(default=timedelta(seconds=0))
    workout1_score = models.IntegerField(default=1)
    workout2_time = models.DurationField(default=timedelta(seconds=0))
    workout2_score = models.IntegerField(default=1)
    workout3_time = models.DurationField(default=timedelta(seconds=0))
    workout3_score = models.IntegerField(default=1)
    workout4_time = models.DurationField(default=timedelta(seconds=0))
    workout4_score = models.IntegerField(default=1)
    points = models.IntegerField(default=4)

    def __str__(self):
        return self.name
