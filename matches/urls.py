from django.urls import path
from .views import MatchDetailView, MatchListView

urlpatterns = [
    path("schedule/", MatchListView, name="match_list"),
    path("schedule/<int:pk>/", MatchDetailView, name="match_detail"),
    
]