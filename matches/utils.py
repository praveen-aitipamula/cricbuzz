from .models import Franchise, Match
from django.shortcuts import render,redirect
from django.db.models import Q



def get_points_table():
    table =[]
    
    franchises = Franchise.objects.all()

    

    for franchise in franchises:
        runs_scored = 0
        overs_faced = 0
        runs_conceded = 0
        overs_bowled = 0

        played = Match.objects.filter(status="Completed").filter(Q(team1=franchise)|Q(team2=franchise)).count()

        won = Match.objects.filter(status="Completed",winner=franchise).count()

        lost = played-won

        points = int(won) * 2

        matches = Match.objects.filter(
            status="Completed"
        ).filter(
            Q(team1=franchise) |
            Q(team2=franchise)
        )

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
                nrr = ( runs_scored / overs_faced ) - (runs_conceded / overs_bowled)
            else:
                nrr = 0

        table.append({
            "team": franchise,
            "played": played,
            "won": won,
            "lost": lost,
            "points": points,
            "nrr": round(nrr,3)
        })
        table = sorted(
            table,
            key=lambda x: (x["points"],x["nrr"]),

            reverse=True
        )

        context={
            "table": table,
        }

    
    return table
