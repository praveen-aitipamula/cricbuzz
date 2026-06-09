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
    winner = models.ForeignKey(Franchise, on_delete=models.SET_NULL, null=True, blank=True, related_name="won_matches")
    team1_score = models.CharField(max_length=20, blank=True, null=True)
    team1_wickets = models.IntegerField(blank=True, null=True)
    team1_overs = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    team2_score = models.CharField(max_length=20, blank=True, null=True)
    team2_wickets = models.IntegerField(blank=True, null=True)  
    team2_overs = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    batting_first = models.ForeignKey(Franchise,on_delete=models.SET_NULL, blank=True, null=True, related_name="batting_first_matches")

    def __str__(self):
        return f"Match {self.match_number}: {self.team1.short_name} vs {self.team2.short_name} at {self.venue.name} on {self.match_date}"