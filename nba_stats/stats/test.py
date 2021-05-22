from urllib.request import urlopen
from bs4 import BeautifulSoup
from basketball_reference_scraper.players import get_stats, get_game_logs, get_player_headshot


def scrape_player_season_data(player_name):
    # print("player name:", player_name)
    url = get_correct_player_page(player_name)[:-5] + "/gamelog/"
    # print("player page:", url)
    season = 2010
    seasons_left = True
    player_logs = []
    while season < 2015:
        print("Season:", season)
        season_url = url + str(season)
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
        season += 1

    for x in player_logs:
        print(x)
    return


def get_correct_player_page(player_name):
    id_num = 1
    match = False
    while not match:
        player_endpoint = get_player_url_endpoint(player_name, id_num)
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


def get_player_url_endpoint(player_name, num):
    first_name, last_name = player_name.split(' ')
    url_endpoint = last_name[0] + '/'
    digit_id = '0' + str(num)
    if len(last_name) < 5:
        url_endpoint += last_name + first_name[:2] + digit_id + '.html'
    else:
        url_endpoint += last_name[:5] + first_name[:2] + digit_id + '.html'

    # print("url_endpoint:", url_endpoint.lower())
    return url_endpoint.lower()


# scrape_player_season_data('Ray Allen')

stats = get_game_logs('Ray Allen', '2010-01-01', '2014-04-01', False)
print(stats)
