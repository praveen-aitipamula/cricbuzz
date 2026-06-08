from .models import Franchise, Match
from django.shortcuts import render,redirect
from django.db.models import Q



def get_points_table():
    table =[]
    
    franchises = Franchise.objects.all()

    

    for franchise in franchises:
        played = Match.objects.filter(status="Completed").filter(Q(team1=franchise)|Q(team2=franchise)).count()

        won = Match.objects.filter(status="Completed",winner=franchise).count()

        lost = played-won

        points = int(won) * 2

        table.append({
            "team": franchise,
            "played": played,
            "won": won,
            "lost": lost,
            "points": points,
            "nrr": nrr
        })
        table = sorted(
            table,
            key=lambda x: x["points"],
            reverse=True
        )

        context={
            "table": table,
        }

    
    return table
