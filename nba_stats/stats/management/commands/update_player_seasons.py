from django.core.management.base import BaseCommand
from ... models import Player, Team, Player_Game
from urllib.request import urlopen
from bs4 import BeautifulSoup


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'Scrapes bball-ref for players stats, adds them to the db if they aren\'t already in there'

    def handle(self, *args, **options):
        # pulls all individual player's stats from each game they played
        # from the 2010 season to current
        self.populate_player_games()

    # NBA seasons typically start in Nov and End in April
    def generate_team_id(team_name, season):
        if int(season[5:7]) >= 10:
            pass

    def populate_player_games(self):
        # Delete all existing records to prevent duplicate entries
        Player_Game.objects.all().delete()
        for player in Player.objects.all():
            player_records = self.scrape_player_season_data(
                player.player_name, player.end_season)
            for game in player_records:
                #Game is DNP
                if len(game) == 9:
                    Player_Game(player_id=player.player_id,
                                game_number=game[0],
                                date=game[2],
                                age=game[3],
                                team_id=pass,
                                away_home=game[5],
                                opponent=pass,
                                result=game[7],
                                dnp=game[8])
                try:
                    Player_Game(
                        player_id=player.player_id,
                        game_number=game[0],
                        date=game[2],
                        age=game[3],
                        team_id=Team.objects.get()
                        opponent=models.ForeignKey(
                            Team, on_delete=models.CASCADE, related_name='opponent')
                        away_home=models.CharField(default=' ', max_length=1)
                        result=models.CharField(default='0', max_length=7)
                        started=models.IntegerField(default='0')
                        # Gametime
                        minutes_played=models.DecimalField(
                            max_digits=4, decimal_places=1, default=0)
                        # Scoring
                        field_goals=models.DecimalField(
                            max_digits=4, decimal_places=1, default=0)
                        field_goals_attempted=models.DecimalField(
                            max_digits=4, decimal_places=1, default=0)
                        field_goals_pct=models.DecimalField(
                            max_digits=4, decimal_places=3, default=0)
                        three_pts=models.DecimalField(
                            max_digits=4, decimal_places=1, default=0)
                        three_pts_attempted=models.DecimalField(
                            max_digits=4, decimal_places=2, default=0)
                        three_pts_pct=models.DecimalField(
                            max_digits=4, decimal_places=3, default=0)
                        points=models.DecimalField(
                            max_digits=4, decimal_places=2, default=0)
                        # Free Throws
                        free_throws=models.DecimalField(
                            max_digits=4, decimal_places=2, default=0)
                        free_throws_attempted=models.DecimalField(
                            max_digits=4, decimal_places=2, default=0)
                        free_throws_pct=models.DecimalField(
                            max_digits=4, decimal_places=3, default=0)
                        # Boards
                        off_reb=models.DecimalField(
                            max_digits=4, decimal_places=2, default=0)
                        def_reb=models.DecimalField(
                            max_digits=4, decimal_places=2, default=0)
                        total_reb=models.DecimalField(
                            max_digits=4, decimal_places=2, default=0)
                        # Assist
                        assists=models.DecimalField(
                            max_digits=4, decimal_places=2, default=0)
                        # Steals
                        steals=models.DecimalField(
                            max_digits=4, decimal_places=2, default=0)
                        # Blocks
                        blocks=models.DecimalField(
                            max_digits=4, decimal_places=2, default=0)
                        # Turnovers
                        turnovers=models.DecimalField(
                            max_digits=4, decimal_places=2, default=0)
                        # Personal Fouls
                        pers_fouls=models.DecimalField(
                            max_digits=4, decimal_places=2, default=0)
                        # GameScore is a measure of productivity developed by John Hollinger
                        # rough measurement similar to points i.e 10 is decent 40 is great
                        game_score=models.DecimalField(
                            max_digits=5, decimal_places=2, default=0)
                        plus_minus=models.IntegerField(default=0)


                    ).save()

            return
        # self.stdout.write(self.style.SUCCESS('Updated/Populated Players'))

    def scrape_player_season_data(self, player_name, end_season, start_season=2010):
        url = self.get_correct_player_page(player_name)[:-5] + "/gamelog/"
        season_to_scrape = start_season
        player_logs = []
        while season_to_scrape < end_season:
            season_url = url + str(season_to_scrape)
            print(season_url)
            html = urlopen(season_url)
            soup = BeautifulSoup(html, features="html.parser")
            table2 = soup.find('table', id="pgl_basic")
            rows = table2.findAll('tr')[1:]

            game_numbers = [[th.getText() for th in rows[i].findAll('th', {"data-stat": "ranker"})]
                            for i in range(len(rows))]

            game_stats = [[td.getText() for td in rows[i].findAll('td')]
                          for i in range(len(rows))]

            # prune empty rows and RK rows
            game_numbers = [row for row in game_numbers if row != ['Rk']]
            player_stats = [row for row in game_stats if row != []]

            for i in range(len(game_numbers)):
                game_numbers[i] += player_stats[i]

            player_logs += game_numbers
            season_to_scrape += 1

        for x in player_logs:
            print(x)

        return

    def get_correct_player_page(self, player_name):
        id_num = 1
        match = False
        while not match:
            player_endpoint = self.get_player_url_endpoint(player_name, id_num)
            try:
                url = 'https://www.basketball-reference.com/players/' + player_endpoint
                html = urlopen(url)
            except:
                match = True

            soup = BeautifulSoup(html, features="html.parser")
            player_page = soup.find('h1', itemprop="name").getText().strip()
            if player_page == player_name:
                return url
            id_num += 1

        return

    def get_player_url_endpoint(self, player_name, num):
        first_name, last_name = player_name.split(' ')
        url_endpoint = last_name[0] + '/'
        digit_id = '0' + str(num)
        if len(last_name) < 5:
            url_endpoint += last_name + first_name[:2] + digit_id + '.html'
        else:
            url_endpoint += last_name[:5] + first_name[:2] + digit_id + '.html'

        return url_endpoint.lower()
