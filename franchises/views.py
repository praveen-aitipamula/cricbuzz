from django.shortcuts import render, get_object_or_404
from .models import  Franchise

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