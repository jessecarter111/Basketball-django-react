from django.core.management.base import BaseCommand
from ... models import Player
from urllib.request import urlopen
from bs4 import BeautifulSoup
import string


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'Scrapes bball-ref for players stats, adds them to the db if they aren\'t already in there'

    def handle(self, *args, **options):
        # Pulls all individual player entries for any active players in years >= 2010
        self.populate_players()

    def populate_players(self):
        # Remove all exisiting entries to prevent duplicates
        Player.objects.all().delete()
        player_data = self.scrape_players()

        for p in player_data:
            # Verify the size of the data frame and that the player was active
            # in 2010 at the earliest, otherwise we don't need to include them
            # p[2] corresponds to the players most recent active year.
            if int(p[2]) >= 2010:
                try:
                    id_string = self.generate_player_id(p[0], p[1])
                    if not Player.objects.filter(player_id=id_string).exists():
                        entry = Player(player_id=id_string, player_name=p[0], draft_year=p[1],
                                       end_year=p[2], position=p[3], height=p[4], weight=p[5], birth_date=p[6])
                        entry.save()
                except:
                    self.stdout.write(self.style.ERROR(p))

        self.stdout.write(self.style.SUCCESS('Updated/Populated Players'))

    # Generates a player id of the form "álex_abrines_2017"
    # using their full name and draft year
    def generate_player_id(self, player_name, player_draft_year):
        id_string = player_name + ' ' + str(player_draft_year)
        return id_string.replace(' ', '_').lower()

    def scrape_players(self):
        # url page to be scraped
        alphabet = list(string.ascii_lowercase)
        player_list = []
        for letter in alphabet:
            url = 'https://www.basketball-reference.com/players/' + letter
            html = urlopen(url)
            soup = BeautifulSoup(html, features="html.parser")
            soup.findAll('tr', limit=2)

            # avoid the first header row
            rows = soup.findAll('tr')[1:]

            # Player names are headers instead of rows, so we need to pull
            # the names and data seperately then concatenate them
            player_names = [[th.getText() for th in rows[i].findAll('th')]
                            for i in range(len(rows))]

            player_stats = [[td.getText() for td in rows[i].findAll('td')]
                            for i in range(len(rows))]

            for i in range(len(rows)):
                player_stats[i] = player_names[i] + player_stats[i]
            player_list += player_stats

        return player_list
