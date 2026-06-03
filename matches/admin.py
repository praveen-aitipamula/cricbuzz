from django.contrib import admin
from .models import Match

# Register your models here.
@admin.register(Match)  
class FranchiseAdmin(admin.ModelAdmin):
    list_display = (
        "team1",
        "team2",
        "venue",
        
    )

    search_fields = (
        "team1__name",
        "team2__name",
        "venue__name",
    )
