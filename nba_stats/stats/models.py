from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related

# Create your models here.


class Franchise(models.Model):
    franchise_id = models.CharField(primary_key=True, max_length=10)
    franchise_name = models.CharField(max_length=50)
    league = models.CharField(max_length=8)
    inaug = models.CharField(max_length=7)
    end = models.CharField(max_length=7)
    years = models.IntegerField()
    games = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    w_l_pct = models.DecimalField(max_digits=3, decimal_places=1)
    playoffs = models.IntegerField()
    division = models.IntegerField()
    conference = models.IntegerField()
    championships = models.IntegerField()


class Team(models.Model):
    franchise_id = models.ForeignKey(Franchise, default=' ', on_delete=CASCADE)
    team_id = models.CharField(default='', primary_key=True, max_length=50)
    season = models.CharField(null=True, max_length=7)
    league = models.CharField(null=True, max_length=7)
    team_name = models.CharField(null=True, max_length=50)
    wins = models.IntegerField(null=True)
    losses = models.IntegerField(null=True)
    w_l_pct = models.DecimalField(null=True, max_digits=5, decimal_places=1)
    finish = models.CharField(null=True, max_length=50)
    srs = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    pace = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    relative_pace = models.DecimalField(
        null=True, max_digits=5, decimal_places=2)
    ortg = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    relative_ortg = models.DecimalField(
        null=True, max_digits=5, decimal_places=2)
    drtg = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    relative_drtg = models.DecimalField(
        null=True, max_digits=5, decimal_places=2)
    playoffs = models.CharField(null=True, max_length=50)
    coaches = models.CharField(null=True, max_length=100)
    top_ws = models.CharField(null=True, max_length=100)

    def __str__(self):
        return ''


class Player(models.Model):
    player_id = models.CharField(primary_key=True, max_length=50, default='0')
    player_name = models.CharField(max_length=100, null=True)
    draft_year = models.IntegerField(null=True)
    end_year = models.IntegerField(null=True)
    position = models.CharField(max_length=5, null=True)
    height = models.CharField(max_length=4, null=True)
    weight = models.IntegerField(null=True)
    birth_date = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.player_name


class Player_Game(models.Model):
    class Meta:
        unique_together = ('player_id', 'date')

    # Meta
    id = models.AutoField(primary_key=True)
    player_id = models.ForeignKey(Player, on_delete=CASCADE)
    game_number = models.IntegerField(default=0)
    date = models.DateField(default=" ")
    age = models.CharField(default="0", max_length=7)
    team_id = models.ForeignKey(Team, on_delete=CASCADE, related_name='team')
    opponent = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='opponent')
    away_home = models.CharField(default=' ', max_length=1)
    result = models.CharField(default='0', max_length=7)
    started = models.IntegerField(default='0')
    # Gametime
    minutes_played = models.DecimalField(
        max_digits=4, decimal_places=1, default=0)
    # Scoring
    field_goals = models.DecimalField(
        max_digits=4, decimal_places=1, default=0)
    field_goals_attempted = models.DecimalField(
        max_digits=4, decimal_places=1, default=0)
    field_goals_pct = models.DecimalField(
        max_digits=4, decimal_places=3, default=0)
    three_pts = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    three_pts_attempted = models.DecimalField(
        max_digits=4, decimal_places=2, default=0)
    three_pts_pct = models.DecimalField(
        max_digits=4, decimal_places=3, default=0)
    points = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    # Free Throws
    free_throws = models.DecimalField(
        max_digits=4, decimal_places=2, default=0)
    free_throws_attempted = models.DecimalField(
        max_digits=4, decimal_places=2, default=0)
    free_throws_pct = models.DecimalField(
        max_digits=4, decimal_places=3, default=0)
    # Boards
    off_reb = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    def_reb = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    total_reb = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    # Assist
    assists = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    # Steals
    steals = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    # Blocks
    blocks = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    # Turnovers
    turnovers = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    # Personal Fouls
    pers_fouls = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    # GameScore is a measure of productivity developed by John Hollinger
    # rough measurement similar to points i.e 10 is decent 40 is great
    game_score = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    plus_minus = models.IntegerField(default=0)
    dnp = models.CharField(default='', max_length=20)
