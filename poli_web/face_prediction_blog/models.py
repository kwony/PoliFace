from django.db import models
from django.utils import timezone


class Politician(models.Model):
    name = models.CharField(max_length=200)
    party = models.CharField(max_length=200, null=True)
    job = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True)
    namu_link = models.CharField(max_length=1000, null=True)
    count = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    political_preference = models.CharField(max_length=200, null=True)
    shot_history = models.TextField(null=True)
    profile_picture = models.ImageField(null=True)

    # To Solve problem with korean letter with ascii code
    # Use this method in the model __unicode__ rather then __str__
    def __unicode__(self):
        return self.name

    def add_politician(self):
        self.save()


class User_Info(models.Model):
    living_area = models.CharField(max_length=200)
    political_preference = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    age = models.IntegerField()

class Picture(models.Model):
    picfile = models.FileField(upload_to='usersUglyFace')