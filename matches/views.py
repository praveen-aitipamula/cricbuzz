from django.shortcuts import redirect, render
from .models import Match
from franchises.models import FranchisePlaying11,MatchPlaying11

def MatchListView(request):
    matches = Match.objects.all()
    context = {"matches": matches}
    return render(request, "match_list.html", context)  

def MatchDetailView(request, pk):
    match = Match.objects.get(pk=pk)
    context = {"match": match}
    return render(request, "match_detail.html", context)

def ManageMatchView(request, pk):
    match = Match.objects.get(id=pk)
    if request.method == "POST":
        team1_xi = FranchisePlaying11.objects.filter(
            franchise=match.team1
        )
        for item in team1_xi:

            MatchPlaying11.objects.get_or_create(
                match=match,
                franchise=match.team1,
                player=item.player
            )

        team2_xi = FranchisePlaying11.objects.filter(
            franchise=match.team2
        )
        for item in team2_xi:

            MatchPlaying11.objects.get_or_create(
                match=match,
                franchise=match.team2,
                player=item.player
            )

        print("Playing XI Created")
        return redirect(
            "match_detail",
            pk=match.id
        )

        
    team1_xi = FranchisePlaying11.objects.filter(
        franchise=match.team1
    )
    team2_xi = FranchisePlaying11.objects.filter(
        franchise=match.team2       
    )
    context = {
        "match": match,                 
        "team1_xi": team1_xi,
        "team2_xi": team2_xi,   
    }
    return render(request, "manage_match.html", context)