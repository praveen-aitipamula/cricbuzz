from django.db import models

from franchises.models import Franchise

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    image = models.ImageField(upload_to="venue_images/", blank=True, null=True)
    capacity = models.PositiveIntegerField(blank=True, null=True)
    home_ground = models.ForeignKey(Franchise, on_delete=models.SET_NULL, blank=True, null=True, related_name="home_venues")
    

    def __str__(self):
        return self.name
