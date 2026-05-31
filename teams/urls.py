from django.urls import path
from .views import teams

urlpatterns = [
    path("", teams, name="teams"),
]