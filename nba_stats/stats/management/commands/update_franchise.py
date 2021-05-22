from django.core.management.base import BaseCommand, CommandError
from ... models import Franchise, Player, Team
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'Scrapes bball-ref for currently active NBA franchises'

    def handle(self, *args, **options):
        # Pulls and populates all currently active NBA franchises
        self.populate_franchises()

    def populate_franchises(self):
        franchises = self.scrape_franchises()
        Franchise.objects.all().delete()
        for franchise in franchises:
            id = self.generate_franchise_id(franchise[0], franchise[2])
            # Checks for existing entries to prevent duplicates
            if not Franchise.objects.filter(franchise_name=franchise[0]).exists():
                franchise_entry = Franchise(franchise_id=id, franchise_name=franchise[0],
                                            league=franchise[1], inaug=franchise[2], end=franchise[3],
                                            years=franchise[4], games=franchise[5], wins=franchise[6],
                                            losses=franchise[7], w_l_pct=franchise[8], playoffs=franchise[9],
                                            division=franchise[10], conference=franchise[11],
                                            championships=franchise[12])
                franchise_entry.save()

        self.stdout.write(self.style.SUCCESS('Updated/Populated Franchises'))

    def generate_franchise_id(self, franchise_name, franchise_inaug):
        # Generates a franchise id in the form "atlanta_hawks_1949-50"
        # using their current full name + their inaugural year as a franchise
        id_string = franchise_name + '_' + franchise_inaug
        return id_string.replace(' ', '_').lower()

    def scrape_franchises(self):
        # We are scraping the rows from the 'Active Teams' table
        html = urlopen("https://www.basketball-reference.com/teams/")

        soup = BeautifulSoup(html, features="html.parser")
        # There are 2 tables on the page, one for active franchises and
        # one for defunct ones, we only want the active franchises so we
        # select the first table.
        first_table = soup.select_one('table:nth-of-type(1)')

        # avoid the first header row, we only want the data
        rows = first_table.findAll('tr')[1:]

        team_stats = [[td.getText() for td in rows[i].findAll(['th', 'td'])]
                      for i in range(0, len(rows))]

        # In the table on BBall refenrence each franchise is listed as well
        # as their previous iterations, which we don't want. So we filter
        # the data to only grab teams active during the 2020 season, i.e
        # the franchise in its current state.
        return list(filter(lambda x: int(x[3][:4]) >= 2020, team_stats))
