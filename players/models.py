from django.db import models
from teams.models import Team

# Create your models here.
class Player(models.Model):
    ROLE_CHOICES = [
        ("BATTER", "Batter"),
        ("BOWLER", "Bowler"),
        ("ALL_ROUNDER", "All-Rounder"),
        ("WK_BATTER", "Batter/Wicket Keeper"),
    ]

    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)


    def __str__(self):
        return self.name
