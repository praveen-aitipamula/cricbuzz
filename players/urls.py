from django.urls import path
from .views import players      
urlpatterns = [
    path("", players, name="players"), 
]