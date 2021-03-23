from urllib.request import urlopen
from bs4 import BeautifulSoup
import string


def scrape_players():
    url = 'https://www.basketball-reference.com/players/a/adebaba01.html'
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


scrape_players()

player_name = 'Bam Adebayo'
first_name, last_name = player_name.split(' ')
url_endpoint = last_name[0] + '/'
print(first_name)
print(last_name)
if len(last_name) < 5:
    url_endpoint += last_name + first_name[:2] + '01' + '.html'
else:
    url_endpoint += last_name[:5] + first_name[:2] + '01' + '.html'

print(url_endpoint)
