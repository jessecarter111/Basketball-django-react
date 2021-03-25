from django.core.management.base import BaseCommand
from ... models import Franchise, Team
from urllib.request import urlopen
from bs4 import BeautifulSoup


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'Scrapes bball-ref for players stats, adds them to the db if they aren\'t already in there'

    team_codes = {'Atlanta Hawks': 'ATL', 'Boston Celtics': 'BOS', 'Brooklyn Nets': 'BRK',
                  'Charlotte Hornets': 'CHO', 'Chicago Bulls': 'CHI', 'Cleveland Cavaliers': 'CLE',
                  'Dallas Mavericks': 'DAL', 'Denver Nuggets': 'DEN', 'Detroit Pistons': 'DET',
                  'Golden State Warriors': 'GSW', 'Houston Rockets': 'HOU', 'Indiana Pacers': 'IND',
                  'Los Angeles Clippers': 'LAC', 'Los Angeles Lakers': 'LAL', 'Memphis Grizzlies': 'MEM',
                  'Miami Heat': 'MIA', 'Milwaukee Bucks': 'MIL', 'Minnesota Timberwolves': 'MIN',
                  'New Orleans Pelicans': 'NOP', 'New York Knicks': 'NYK', 'Oklahoma City Thunder': 'OKC',
                  'Orlando Magic': 'ORL', 'Philadelphia 76ers': 'PHI', 'Phoenix Suns': 'PHO',
                  'Portland Trail Blazers': 'POR', 'Sacramento Kings': 'SAC', 'San Antonio Spurs': 'SAS',
                  'Toronto Raptors': 'TOR', 'Utah Jazz': 'UTA', 'Washington Wizards': 'WAS'}

    def handle(self, *args, **options):
        self.populate_team_seasons()

    def populate_team_seasons(self):
        # Remove any pre-existing entries to prevent duplicates
        Team.objects.all().delete()
        # team_codes contains a mapping of all active team names and
        # their abbreviations used by bball reference
        for team in self.team_codes.keys():
            url = 'https://www.basketball-reference.com/teams/' + \
                self.team_codes[team]
            # we need to link each team_season to it's corresponding
            # franchise, so we pull the franchise object that matches the
            # the team name
            franchise = Franchise.objects.get(franchise_name=team)
            try:
                team_data = self.scrape_franchise_seasons(url)
            except:
                print(url)

            for season in team_data:
                id = self.generate_team_id(team, season[0])
                if not Team.objects.filter(team_id=id).exists():
                    team_season_entry = Team(team_id=id, franchise_id=franchise, season=season[0],
                                             league=season[1], team_name=season[2], wins=season[3],
                                             losses=season[4], w_l_pct=season[5], finish=season[6],
                                             srs=season[7], pace=season[8], relative_pace=season[9],
                                             ortg=season[10], relative_ortg=season[11], drtg=season[12],
                                             relative_drtg=season[13], playoffs=season[14],
                                             coaches=season[15], top_ws=season[16])

                    team_season_entry.save()

        self.stdout.write(self.style.SUCCESS('Updated/Populated Team Seasons'))

    # Generates a team id of the form "atl_2020-21", using the corresponding
    # season and team_abreviation
    def generate_team_id(self, team_name, team_season):
        id_string = self.team_codes[team_name] + ' ' + team_season
        return id_string.replace(' ', '_').lower()

    def scrape_franchise_seasons(self, url):
        html = urlopen(url)

        soup = BeautifulSoup(html, features="html.parser")

        # avoid the first header row
        rows = soup.findAll('tr')[1:]

        team_stats = [[td.getText() for td in rows[i].findAll(['th', 'td'])]
                      for i in range(0, len(rows))]

        for x in team_stats:
            # These are empty columns used for styling that need to be pruned
            del x[8]
            del x[14]

        # the first column of the data frame x[0] corresponds to the season
        # so we just need to filter out any team records prior to 2010
        return list(filter(lambda x: int(x[0][:4]) >= 2010, team_stats))
