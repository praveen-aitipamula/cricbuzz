from django.contrib import admin

# Register your models here.
from .models import Venue
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "capacity", "home_ground")
    search_fields = ("name", "city")
    list_filter = ("name","city",)     




