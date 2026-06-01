from django.shortcuts import render

# Create your views here.
from .models import Player
def players(request):
    players = Player.objects.all()
    return render(request, "players.html", {"players": players})      
