from django.core.management.base import BaseCommand, CommandError
from ... models import Player, Team


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'Scrapes bball-ref for players stats, adds them to the db if they aren\'t already in there'

    def handle(self, *args, **options):
        # pulls all individual players stats from the 2020 season from bball-reference
        for x in Player.objects.all():
            x.refresh_from_db()
        for x in Team.objects.all():
            x.refresh_from_db()
