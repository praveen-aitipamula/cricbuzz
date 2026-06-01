from django.contrib import admin

# Register your models here.
from .models import Player
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "team",
        "role",
    )

    search_fields = (
        "name",
        "team__name",
        "role",
    )