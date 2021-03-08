from django.db import models

# Create your models here.


class Team(models.Model):
    team_name = models.CharField(max_length=100)
    team_abrev = models.CharField(max_length=3)
    league = models.CharField(max_length=7)
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

    def __str__(self) -> str:
        return self.team_name


class Player(models.Model):
    # Meta
    player_name = models.CharField(max_length=100)
    position = models.CharField(max_length=5)
    age = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # Gametime
    games = models.IntegerField()
    games_started = models.IntegerField()
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
    two_pts = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    two_pts_attempted = models.DecimalField(
        max_digits=4, decimal_places=1, default=0)
    two_pts_pct = models.DecimalField(
        max_digits=4, decimal_places=3, default=0)
    effective_fg_pct = models.DecimalField(
        max_digits=4, decimal_places=1, default=0)
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

    def __str__(self) -> str:
        return self.player_name
