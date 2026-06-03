from django.shortcuts import render
from .models import Match

def MatchListView(request):
    matches = Match.objects.all()
    context = {"matches": matches}
    return render(request, "match_list.html", context)  
def MatchDetailView(request, pk):
    match = Match.objects.get(pk=pk)
    context = {"match": match}
    return render(request, "match_detail.html", context)
