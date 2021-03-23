from django.db import models
from django.db.models.deletion import CASCADE

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
    model_type = models.CharField(default="team", max_length=50)

    def __str__(self):
        return self.team_abrev


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


class Season(models.Model):
    # Meta
    player_id = models.ForeignKey(Player, on_delete=CASCADE)
    season = models.CharField(primary_key=True, max_length=7)
    age = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    league = models.CharField(max_length=4)
    position = models.CharField(max_length=5)
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
        max_digits=4, decimal_places=3, default=0)
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
    points = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    model_type = models.CharField(default="player_stats", max_length=50)


class Career(models.Model):
    # Meta
    player_id = models.ForeignKey(Player, on_delete=CASCADE)
    league = models.CharField(max_length=4)
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
        max_digits=4, decimal_places=3, default=0)
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
    points = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    model_type = models.CharField(default="career_stats", max_length=50)
