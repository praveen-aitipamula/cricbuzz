from django.urls import path
from .views import ipl_player_detail, player_detail, players      
urlpatterns = [
    path("", players, name="players"), 
    path("<int:player_id>/", player_detail, name="player_detail"),
    path("ipl_players/<int:player_id>/", ipl_player_detail, name="ipl_player_detail"),
    
    
    
]
