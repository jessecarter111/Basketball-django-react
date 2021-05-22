from django.core.management.base import BaseCommand
from ... models import Player, Team, Player_Game
from urllib.request import urlopen
from bs4 import BeautifulSoup
from ... utils import clean_name


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'Scrapes bball-ref for players stats, adds them to the db if they aren\'t already in there'

    def handle(self, *args, **options):
        # pulls all individual player's stats from each game they played
        # from the 2010 season to current
        self.populate_player_games()

    def populate_player_games(self):
        # Delete all existing records to prevent duplicate entries
        Player_Game.objects.all().delete()

        for player in Player.objects.all():
            if player.end_year >= 2020:
                try:
                    start_season = 2020
                    player_records = self.scrape_player_season_data(
                        player.player_name, start_season, player.end_year)
                    self.stdout.write(self.style.SUCCESS(
                        'Succesfully got ' + player.player_name + ' records'))
                except Exception as e:
                    print(e)
                    self.stdout.write(self.style.ERROR(
                        'Failed to get ' + player.player_name + ' records'))
                    continue
            else:
                continue
            for game in player_records:
                team = game[5].lower() + '_' + game[0]
                team = Team.objects.get(team_id=team)
                opponent = game[7].lower() + '_' + game[0]
                opponent = Team.objects.get(team_id=opponent)

                if len(game) <= 10:
                    # Game is a DNP if len <= 10
                    try:
                        Player_Game(player_id=player, season=game[0], game_number=game[1],
                                    date=game[3], age=game[4], team_id=team,
                                    away_home=game[6], opponent_id=opponent, result=game[8],
                                    dnp=game[9]).save()
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(
                            '*************************************************'))
                        print("DNP")
                        print(len(game), game)
                        self.stdout.write(self.style.ERROR(e))
                        self.stdout.write(self.style.ERROR(
                            '*************************************************'))
                else:
                    # If len > 10 the Player dressed so all stats are available
                    try:
                        game_time = game[10].replace(":", ".")
                        Player_Game(
                            player_id=player, season=game[0], game_number=game[1],
                            date=game[3], age=game[4], team_id=team,
                            opponent_id=opponent, away_home=game[6], result=game[8],
                            started=game[9], minutes_played=game_time,
                            field_goals=game[11], field_goals_attempted=game[12],
                            field_goals_pct=game[13] if game[13] else 0,
                            three_pts=game[14], three_pts_attempted=game[15],
                            three_pts_pct=game[16] if game[16] else 0,
                            free_throws=game[17], free_throws_attempted=game[18],
                            free_throws_pct=game[19] if game[19] else 0,
                            off_reb=game[20], def_reb=game[21], total_reb=game[22],
                            assists=game[23], steals=game[24], blocks=game[25],
                            turnovers=game[26], pers_fouls=game[27], points=game[28],
                            game_score=game[29], plus_minus=game[30]).save()

                    except Exception as e:
                        self.stdout.write(self.style.ERROR(
                            '*************************************************'))
                        print("Played")
                        print(len(game), game)
                        self.stdout.write(self.style.ERROR(e))
                        self.stdout.write(self.style.ERROR(
                            '*************************************************'))

            self.stdout.write(self.style.SUCCESS(
                'Succesfully added ' + player.player_name + ' records'))
        self.stdout.write(self.style.SUCCESS('Updated/Populated Player Games'))

    def scrape_player_season_data(self, player_name, start_season, end_season):
        url = self.get_correct_player_page(player_name)[:-5] + "/gamelog/"
        season_to_scrape = start_season
        player_logs = []
        while season_to_scrape <= end_season:
            # Need to preppend the season in the form '2020-21'
            # to each row so the team_id's can be easily parsed
            # as they are of the form 'atl_2020-21'
            season_id = str(season_to_scrape - 1) + '-' + \
                str(season_to_scrape)[-2:]

            season_url = url + str(season_to_scrape)
            html = urlopen(season_url)
            soup = BeautifulSoup(html, features="html.parser")
            table2 = soup.find('table', id="pgl_basic")
            rows = table2.findAll('tr')[1:]

            game_numbers = [[th.getText() for th in rows[i].findAll('th', {"data-stat": "ranker"})]
                            for i in range(len(rows))]

            game_stats = [[td.getText() for td in rows[i].findAll('td')]
                          for i in range(len(rows))]

            for i in range(len(game_numbers)):
                game_numbers[i] = [season_id] + game_numbers[i]
                game_numbers[i] += game_stats[i]

            player_logs += game_numbers
            season_to_scrape += 1

        player_logs = [log for log in player_logs if len(log) > 2]

        return player_logs

    def get_correct_player_page(self, player_name):
        id_num = 1
        match = False
        while not match:
            player_endpoint = self.get_player_url_endpoint(player_name, id_num)
            try:
                url = 'https://www.basketball-reference.com/players/' + player_endpoint
                html = urlopen(url)
            except:
                self.stdout.write(self.style.ERROR(url))
                return False

            soup = BeautifulSoup(html, features="html.parser")
            # Verify that the current page is the correct player page
            # as there may be collisions in endpoints ex. 'Randy Allen'
            # and 'Ray Allen' both result in 'allenra'
            player_page = soup.find('h1', itemprop="name").getText().strip()
            if clean_name(player_page) == clean_name(player_name):
                return url
            id_num += 1

        return False

    def get_player_url_endpoint(self, player_name, num):
        first_name, last_name = player_name.split(' ')
        # Need to remove diacritics from frist and last name
        # as the basketball reference urls only contain
        # regular ascii chars
        first_name = clean_name(first_name)
        last_name = clean_name(last_name)

        url_endpoint = last_name[0] + '/'
        digit_id = '0' + str(num)

        # Player url endpoints are of the form 'allenra01' taking up to
        # the first 5 letters of their last name and the first 2 letters of
        # their first name + a numerical indicator in case of collisions.
        if len(last_name) < 5:
            url_endpoint += last_name + first_name[:2] + digit_id + '.html'
        else:
            url_endpoint += last_name[:5] + first_name[:2] + digit_id + '.html'

        return url_endpoint.lower()
