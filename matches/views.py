from multiprocessing import context

from django.shortcuts import redirect, render

from franchises.views import franchise
from .models import Match, Franchise
from franchises.models import FranchisePlaying11,MatchPlaying11
from django.db.models import Q
from .utils import get_points_table

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

        match.status = "Playing11 Confirmed"
        match.save()
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

def MatchResultView(request, pk):
    match = Match.objects.get(id=pk)
    if request.method == "POST":
        match.team1_score = int(request.POST.get("team1_score"))
        match.team1_wickets = int(request.POST.get("team1_wickets"))
        match.team1_overs = request.POST.get("team1_overs")
        match.team2_score = int(request.POST.get("team2_score"))
        match.team2_wickets = int(request.POST.get("team2_wickets"))
        match.team2_overs = request.POST.get("team2_overs")
        match.batting_first_id = request.POST.get("batting_first")

        if match.batting_first == match.team1:
            if match.team1_score > match.team2_score:
                match.winner = match.team1
                match.result = (
                    f"{match.team1.short_name} won by "
                    f"{match.team1_score - match.team2_score -1} runs"
                )
            else:
                wickets_remaning = 10 - match.team2_wickets
                match.winner = match.team2
                match.result =(
                    f"{match.team2.short_name} won by "
                    f"{wickets_remaning} wickets"
                )
        else:
            if match.team2_score > match.team1_score:
                match.winner = match.team2
                match.result=(
                    f"{match.team2.short_name} won by "
                    f"{match.team2_score - match.team1_score-1} runs"
                )
            else:
                wickets_remaning = 10 - match.team1_wickets
                match.winner = match.team1
                match.result=(
                    f"{match.team1.short_name} won by "
                    f"{wickets_remaning} wickets"
                )

        # if match.team1_score > match.team2_score:   
        #     match.winner = match.team1
        #     match.result = (
        #         f"{match.team1.short_name} won by "
        #         f"{match.team1_score - match.team2_score} runs"
        #     )

        # else:

        #     match.winner = match.team2

        #     wickets_remaining = (
        #         10 - int(request.POST.get("team2_wickets"))
        #     )

        #     match.result = (
        #         f"{match.team2.short_name} won by "
        #         f"{wickets_remaining} wickets"
        #     )


        
        
        
        match.status = "Completed"
        match.save()
        return redirect(
            "match_detail",
            pk=match.id
        )
    context = {
        "match": match,
    }
    return render(request, "match_result.html", context)
    

def PointsTableView(request):
    table = get_points_table()
    
    context={
        "table":table
    }
    
    return render(request,"points_table.html",context)

