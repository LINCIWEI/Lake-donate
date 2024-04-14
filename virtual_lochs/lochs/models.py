from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Loch(models.Model):
    ObjectID = models.IntegerField()
    LochCode = models.TextField()
    SurfaceArea = models.FloatField()
    AuthID = models.TextField()
    LochAuth = models.TextField()
    IslandName = models.TextField()
    LochName = models.TextField()
    Price = models.IntegerField()

    def __str__(self):
        return self.ObjectID, self.LochCode, self.SurfaceArea, self.SAuthID, self.LochAuth, 
        self.IslandName, self.LochName, self.Price