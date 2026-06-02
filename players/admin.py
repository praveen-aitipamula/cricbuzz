from django.contrib import admin

# Register your models here.
from .models import Player, IPL_Player
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "team",
        "role",
    )
    list_filter = (
        "team",
        "role",
    )


    search_fields = (
        "name",
        "team__name",
    
    )

@admin.register(IPL_Player)
class IPLPlayerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
       
    )
    list_filter = (
        "country",
        "name",
    )


    search_fields = (
        "name",
        
    
    )
