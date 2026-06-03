from django.db import models

# Create your models here.
from franchises.models import Franchise
from venues.models import Venue

class Match(models.Model):
    match_number = models.IntegerField()
    team1 = models.ForeignKey(Franchise, on_delete=models.CASCADE, related_name="home_matches")
    team2 = models.ForeignKey(Franchise, on_delete=models.CASCADE, related_name="away_matches")
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    match_date = models.DateField()
    status = models.CharField(max_length=50, default="Scheduled")

    def __str__(self):
        return f"Match {self.match_number}: {self.team1.short_name} vs {self.team2.short_name} at {self.venue.name} on {self.match_date}"