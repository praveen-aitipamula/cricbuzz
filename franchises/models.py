from django.db import models
from players.models import IPL_Player
# Create your models here.
class Franchise(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    logo = models.ImageField(
        upload_to="franchise_logos/",
        blank=True,
        null=True
    )
    

    def __str__(self):
        return self.short_name
    
class FranchiseSquad(models.Model):
    franchise = models.ForeignKey(Franchise, on_delete=models.CASCADE,related_name="squad")
    player = models.ForeignKey(IPL_Player, on_delete=models.CASCADE)

    class Meta:

        constraints = [
            models.UniqueConstraint(
                fields=["player"],
                name="unique_player_team"
            )
        ]

    def __str__(self):
        return f"{self.franchise.short_name} - {self.player.name}"

class FranchisePlaying11(models.Model):
    franchise = models.ForeignKey(Franchise, on_delete=models.CASCADE, related_name="playing11")
    player = models.ForeignKey(IPL_Player, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["player"],
                name="unique_player_playing11"
            )
        ]

    def __str__(self):
        return f"{self.franchise.short_name} - {self.player.name}"