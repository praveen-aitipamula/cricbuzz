from django.contrib import admin


# Register your models here.
from .models import Franchise, FranchisePlaying11, FranchiseSquad
@admin.register(Franchise)  
class FranchiseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "short_name",
    )

    search_fields = (
        "name",
        "short_name",
    )

@admin.register(FranchiseSquad)
class FranchiseSquadAdmin(admin.ModelAdmin):
    list_display = (
        "franchise",
        "player",
    )

    search_fields = (
        "franchise__name",
        "player__name",
    )

@admin.register(FranchisePlaying11)
class FranchisePlaying11Admin(admin.ModelAdmin):
    list_display = (
        "franchise",
        "player",
    )

    search_fields = (
        "franchise__name",
        "player__name",
    )

