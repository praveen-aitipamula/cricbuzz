from django.urls import path

from .views import franchise, franchise_detail
urlpatterns = [
    path("", franchise, name="franchise"),
    path("<int:franchise_id>/", franchise_detail, name="franchise_detail"),
]