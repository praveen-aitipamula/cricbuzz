from django.shortcuts import render
from matches.utils import get_points_table
from matches.models import Match


# Create your views here.
def home(request):
    matches = Match.objects.filter(
        status="Completed"
    ).order_by("-id")[:3]

    upcoming_matches = Match.objects.filter(
        status="Scheduled"
    ).order_by("id")[:5]

    



    table = get_points_table()
    context ={
        "matches":matches,
        "table":table,
        "upcoming_matches": upcoming_matches,
    }
    return render(request, "home.html",context)