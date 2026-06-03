from django.urls import path

from .views import franchise, franchise_detail, franchise_playing11
urlpatterns = [
    path("", franchise, name="franchise"),
    path("<int:franchise_id>/", franchise_detail, name="franchise_detail"),
    path("<int:franchise_id>/playing11/", franchise_playing11, name="franchise_playing11"),
]