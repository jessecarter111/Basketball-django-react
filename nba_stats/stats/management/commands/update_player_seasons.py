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

    def populate_player_seasons(self):
        pass
        # for player_entity in Player.objects.values_list('player_id', 'player_name').order_by('player_id')
        # the headers of the data are the column names
        # headers = data[0]
        # the players data is their stats indexed in the same order as the headers
        # fields = Player._meta.fields

        # cleaning data so fields are not null

        # for p in player_data:
        #     if len(p) <= 8:
        #         try:
        #             id_string = generate_player_id(p[0], p[1])
        #             if not Player.objects.filter(player_id=id_string).exists():
        #                 entry = Player(player_id=id_string, player_name=p[0], draft_year=p[1],
        #                                end_year=p[2], position=p[3], height=p[4], weight=p[5], birth_date=p[6])
        #                 entry.save()
        #         except:
        #             self.stdout.write(self.style.ERROR(p))

        # self.stdout.write(self.style.SUCCESS('Updated/Populated Players'))


def scrape_player_season_data(player_name):
    player_endpoint = get_player_url_endpoint(player_name)

    url = 'https://www.basketball-reference.com/players/' + player_endpoint
    html = urlopen(url)
    soup = BeautifulSoup(html, features="html.parser")
    soup.findAll('tr', limit=2)

    headers = [th.getText()
               for th in soup.findAll('tr', limit=2)[0].findAll('th')]

    print(headers)

    rows = soup.findAll('tr')[1:]

    seasons = [[th.getText() for th in rows[i].findAll('th')]
               for i in range(len(rows))]

    player_stats = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]

    for i in range(len(seasons)):
        seasons[i] += player_stats[i]

    return seasons


def get_player_url_endpoint(player_name):
    first_name, last_name = player_name.split(' ')
    url_endpoint = last_name[0] + '/'

    if len(last_name) < 5:
        url_endpoint += last_name + first_name[:2] + '01' + '.html'
    else:
        url_endpoint += last_name[:5] + first_name[:2] + '01' + '.html'

    return url_endpoint.lower()
