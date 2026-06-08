from multiprocessing import context

from django.shortcuts import redirect, render

from franchises.views import franchise
from matches.utils import get_points_table
from .models import Match, Franchise
from franchises.models import FranchisePlaying11,MatchPlaying11
from django.db.models import Q
from matches.utils import get_points_table

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
        if match.team1_score > match.team2_score:   
            match.winner = match.team1
            match.result = (
                f"{match.team1.short_name} won by "
                f"{match.team1_score - match.team2_score} runs"
            )

        else:

            match.winner = match.team2

            wickets_remaining = (
                10 - int(request.POST.get("team2_wickets"))
            )

            match.result = (
                f"{match.team2.short_name} won by "
                f"{wickets_remaining} wickets"
            )


        
        
        
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
<<<<<<< Updated upstream
    table =[]
    
    franchises = Franchise.objects.all()

    

    for franchise in franchises:
        played = Match.objects.filter(status="Completed").filter(Q(team1=franchise)|Q(team2=franchise)).count()

        won = Match.objects.filter(status="Completed",winner=franchise).count()

        lost = played-won

        points = int(won) * 2

        runs_scored = 0
        overs_faced = 0
        runs_conceded = 0
        overs_bowled = 0

        matches = Match.objects.filter(status="Completed").filter(Q(team1=franchise)|Q(team2=franchise))
        for match in matches:
            if franchise == match.team1:
                runs_scored += int(match.team1_score)
                overs_faced += float(match.team1_overs)

                runs_conceded += int(match.team2_score)
                overs_bowled += float(match.team2_overs)
            else:
                runs_scored += int(match.team2_score)
                overs_faced += float(match.team2_overs)

                runs_conceded += int(match.team1_score)
                overs_bowled += float(match.team1_overs)

            if overs_faced > 0 and overs_bowled > 0:
                nrr= (runs_scored/overs_faced)-(runs_conceded/overs_bowled)
            else:
                nrr = 0


        table.append({
            "team": franchise,
            "played": played,
            "won": won,
            "lost": lost,
            "points": points,
            "nrr":round(nrr,3)
        })
        table = sorted(
            table,
            key=lambda x: (x["points"],x["nrr"]),
            reverse=True
        )

        context={
            "table": table,
        }

=======
    table = get_points_table()
    context={
        "table":table
    }
>>>>>>> Stashed changes
    
    return render(request,"points_table.html",context)

