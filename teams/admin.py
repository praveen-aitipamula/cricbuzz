from django.contrib import admin

# Register your models here.
from .models import Team
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "short_name",
        
    )

    search_fields = (
        "name",
        "short_name",
    )
