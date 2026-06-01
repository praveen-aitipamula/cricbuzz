from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    flag = models.ImageField(
        upload_to="team_flags/",
        blank=True,
        null=True
    )
    

    def __str__(self):
        return self.short_name
