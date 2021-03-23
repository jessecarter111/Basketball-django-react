from django.core.management.base import BaseCommand, CommandError
from ... models import Player
from urllib.request import urlopen
from bs4 import BeautifulSoup
import string


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'Scrapes bball-ref for players stats, adds them to the db if they aren\'t already in there'

    def handle(self, *args, **options):
        # pulls all individual players stats from the 2020 season from bball-reference
        self.populate_players()

    def populate_players(self):

        def generate_player_id(player_name, player_draft_year):
            id_string = player_name + ' ' + str(player_draft_year)
            return id_string.replace(' ', '_')

        player_data = self.scrape_players()
        # the headers of the data are the column names
        # headers = data[0]
        # the players data is their stats indexed in the same order as the headers
        # fields = Player._meta.fields

        # cleaning data so fields are not null

        for p in player_data:
            # for i, x in enumerate(p):
            #     if p[i] == '':
            #         p[i] = '0'
            # Data verification, check that the player data frame is correctly sized
            if len(p) <= 8:
                try:
                    id_string = generate_player_id(p[0], p[1])
                    if not Player.objects.filter(player_id=id_string).exists():
                        entry = Player(player_id=id_string, player_name=p[0], draft_year=p[1],
                                       end_year=p[2], position=p[3], height=p[4], weight=p[5], birth_date=p[6])
                        entry.save()
                except:
                    self.stdout.write(self.style.ERROR(p))

        self.stdout.write(self.style.SUCCESS('Updated/Populated Players'))

    def scrape_players(self):
        # url page to be scraped
        alphabet = list(string.ascii_lowercase)
        player_list = []

        for letter in alphabet:
            url = 'https://www.basketball-reference.com/players/' + letter
            html = urlopen(url)
            soup = BeautifulSoup(html, features="html.parser")
            soup.findAll('tr', limit=2)

            headers = [th.getText()
                       for th in soup.findAll('tr', limit=2)[0].findAll('th')]

            # avoid the first header row
            rows = soup.findAll('tr')[1:]

            player_names = [[th.getText() for th in rows[i].findAll('th')]
                            for i in range(len(rows))]

            player_stats = [[td.getText() for td in rows[i].findAll('td')]
                            for i in range(len(rows))]

            for i in range(len(rows)):
                player_stats[i] = player_names[i] + player_stats[i]

            player_list += player_stats

        return player_list
