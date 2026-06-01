from django.urls import path
from .views import team_detail, teams

urlpatterns = [
    path("", teams, name="teams"),
    path("<int:team_id>/", team_detail, name="team_detail"),
]