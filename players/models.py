from tkinter import OFF

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
    BATTING_STYLE_CHOICES = [
        ("RIGHT_HANDED", "Right-handed"),   
        ("LEFT_HANDED", "Left-handed"),
        
    ]
    BOWLING_STYLE_CHOICES = [
        ("RIGHT_ARM_FAST", "Right-arm Fast"),
        ("LEFT_ARM_FAST", "Left-arm Fast"),
        ("RIGHT_ARM_MEDIUM", "Right-arm Medium"),
        ("LEFT_ARM_MEDIUM", "Left-arm Medium"),
        ("RIGHT_ARM_OFF_BREAK", "Right-arm Off Break"),
        ("LEFT_ARM_OFF_BREAK", "Left-arm Off Break"),
        ("RIGHT_ARM_LEG_BREAK", "Right-arm Leg Break"),
        ("LEFT_ARM_LEG_BREAK", "Left-arm Leg Break"),
        ("SPIN", "Spin"),
        ("OFF_SPIN", "Off Spin"),
        ("LEG_SPIN", "Leg Spin"),
        ("LEFT_ARM_SPIN", "Left-arm Spin"),
        ("RIGHT_ARM_SPIN", "Right-arm Spin"),
        ("OTHER", "Other"),
    ]

    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    image = models.ImageField(upload_to="player_images/",blank=True,null=True)
    jersey_number = models.PositiveIntegerField(blank=True,null=True)
    date_of_birth = models.DateField(blank=True,null=True)
    batting_style = models.CharField(max_length=50, choices=BATTING_STYLE_CHOICES, blank=True)
    bowling_style = models.CharField(max_length=50, choices=BOWLING_STYLE_CHOICES, blank=True)
    bio = models.TextField(blank=True)


    def __str__(self):
        return self.name


class IPL_Player(models.Model):
    ROLE_CHOICES = [
        ("BAT", "Batter"),
        ("BOWL", "Bowler"),
        ("AR", "All Rounder"),
        ("WK", "Wicket Keeper"),
    ]
    BATTING_STYLE_CHOICES = [
        ("RH", "Right-handed"),   
        ("LH", "Left-handed"),
        
    ]
    BOWLING_STYLE_CHOICES = [
        ("RF", "Right-arm Fast"),
        ("LF", "Left-arm Fast"),
        ("RM", "Right-arm Medium"),
        ("LM", "Left-arm Medium"),
        ("RO", "Right-arm Off Break"),
        ("LO", "Left-arm Off Break"),
        ("RL", "Right-arm Leg Break"),
        ("LL", "Left-arm Leg Break"),
        ("SPIN", "Spin"),
        ("OFF_SPIN", "Off Spin"),
        ("LEG_SPIN", "Leg Spin"),
        ("LEFT_ARM_SPIN", "Left-arm Spin"),
        ("RIGHT_ARM_SPIN", "Right-arm Spin"),
        ("OTHER", "Other"),
    ]

    name = models.CharField(max_length=100)

    country = models.CharField(max_length=50)

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES
    )

    batting_style = models.CharField(
        max_length=50,
        choices=BATTING_STYLE_CHOICES,
        blank=True
    )

    bowling_style = models.CharField(
        max_length=50,
        choices=BOWLING_STYLE_CHOICES,
        blank=True
    )

    image = models.ImageField(
        upload_to="ipl_player_images/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
