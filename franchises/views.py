from django.shortcuts import render, get_object_or_404
from .models import  Franchise, FranchisePlaying11, FranchiseSquad

# Create your views here.
def franchise(request):
    franchises = Franchise.objects.all()
    return render(request, "franchise.html", {"franchises": franchises})

def franchise_detail(request, franchise_id):
    franchise = get_object_or_404(Franchise, id=franchise_id)
    squad = franchise.squad.select_related(
        "player"
    )
    context = {
        "franchise": franchise,
        "squad": squad
    }
    return render(request, "franchise_detail.html", context)

def franchise_playing11(request, franchise_id):
    franchise = get_object_or_404(Franchise, id=franchise_id)
    playing11 = franchise.playing11.select_related(
        "player"
    )
    context = {
        "franchise": franchise,
        "playing11": playing11
    }
    return render(request, "franchise_playing11.html", context) 