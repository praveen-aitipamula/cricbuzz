from django.shortcuts import render

from venues.models import Venue

# Create your views here.
def venue_list(request):
    venues = Venue.objects.all()
    context = {"venues": venues}
    return render(request, "venue_list.html", context)

def venue_detail(request, pk):
    venue = Venue.objects.get(pk=pk)
    context = {"venue": venue}
    return render(request, "venue_detail.html", context)