from django.shortcuts import render, get_object_or_404

import players

# Create your views here.
from .models import Team

def teams(request):
    teams = Team.objects.all()
    return render(request, "teams.html", {"teams": teams})
def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    players = team.player_set.all() 
    context = {
        "team": team,
        "players": players
    } # Get players associated with the team 
    return render(request, "team_detail.html", context)   
  

    


    