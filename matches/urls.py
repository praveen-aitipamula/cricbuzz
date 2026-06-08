from django.urls import path
from .views import ManageMatchView, MatchDetailView, MatchListView, MatchResultView,PointsTableView

urlpatterns = [
    path("schedule/", MatchListView, name="match_list"),
    path("schedule/<int:pk>/", MatchDetailView, name="match_detail"),
    path("<int:pk>/manage", ManageMatchView, name="manage_match"),
    path("<int:pk>/result", MatchResultView, name="match_result"),
    path("pointstable/",PointsTableView,name="points_table"),

    
]