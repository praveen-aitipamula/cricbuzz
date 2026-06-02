from django.urls import path
from .views import player_detail, players      
urlpatterns = [
    path("", players, name="players"), 
    path("<int:player_id>/", player_detail, name="player_detail"),
]