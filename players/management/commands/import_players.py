import csv

from django.core.management.base import BaseCommand

from players.models import IPL_Player 


class Command(BaseCommand):

    help = "Import players from csv"

    def handle(self, *args, **kwargs):

        with open(
            "ipl_2026.csv",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                IPL_Player.objects.create(
                    name=row["name"],
                    country=row["country"],
                    role=row["role"],
                    batting_style=row["batting_style"],
                    bowling_style=row["bowling_style"],

                    image=f"ipl_player_images/{row['image']}"
                )

        self.stdout.write(
            self.style.SUCCESS(
                "Players imported successfully"
            )
        )