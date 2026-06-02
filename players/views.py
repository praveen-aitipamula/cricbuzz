from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Player
def players(request):
    players = Player.objects.all()
    return render(request, "players.html", {"players": players})      

def player_detail(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    context = {
        "player": player,
    }
    return render(request, "player_detail.html", context)
