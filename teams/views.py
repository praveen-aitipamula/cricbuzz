from django.shortcuts import render

# Create your views here.
from .models import Team

def teams(request):
    teams = Team.objects.all()
    return render(request, "teams.html", {"teams": teams})
    