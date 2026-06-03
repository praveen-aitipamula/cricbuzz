import csv

from django.core.management.base import BaseCommand

from franchises.models import Franchise, FranchisePlaying11
from players.models import IPL_Player as Player


class Command(BaseCommand):

    help = "Import Default Playing XI"

    def handle(self, *args, **kwargs):

        with open(
            "playing11.csv",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                franchise_code = row["franchise"].strip()
                player_name = row["player"].strip()

                if not franchise_code or not player_name:
                    continue

                try:
                    franchise = Franchise.objects.get(
                        short_name=franchise_code
                    )

                except Franchise.DoesNotExist:

                    self.stdout.write(
                        self.style.ERROR(
                            f"Franchise not found: {franchise_code}"
                        )
                    )

                    continue

                try:
                    player = Player.objects.get(
                        name=player_name
                    )

                except Player.DoesNotExist:

                    self.stdout.write(
                        self.style.ERROR(
                            f"Player not found: {player_name}"
                        )
                    )

                    continue

                FranchisePlaying11.objects.get_or_create(
                    franchise=franchise,
                    player=player
                )

                

        self.stdout.write(
            self.style.SUCCESS(
                "Playing XI import completed."
            )
        )