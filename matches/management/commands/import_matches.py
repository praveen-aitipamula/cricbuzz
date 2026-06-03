import csv
from datetime import datetime

from django.core.management.base import BaseCommand

from matches.models import Match

from franchises.models import Franchise

from venues.models import Venue

class Command(BaseCommand):
    help = "Import IPL Schedule"
    def handle(self, *args, **kwargs):

        with open(
            "matches.csv",
            encoding="utf-8"
        ) as file:
            reader = csv.DictReader(file)

            for row in reader:
                team1 = Franchise.objects.get(name=row["team1"])
                team2 = Franchise.objects.get(name=row["team2"])
                venue = Venue.objects.get(name=row["venue"])
                match_date = datetime.strptime(row["match_date"], "%d-%m-%Y").date()

                Match.objects.create(
                    match_number=row["match_number"],
                    team1=team1, 
                    team2=team2, 
                    venue=venue, 
                    match_date=match_date
                )
        
        
        self.stdout.write(
            self.style.SUCCESS(
                "Schedule imported successfully"
            )
        )
