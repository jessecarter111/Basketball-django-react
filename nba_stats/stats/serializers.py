from rest_framework import serializers
from .models import Team, Player


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('team_name', 'team_abrev', 'league', 'inaug',
                  'end', 'years', 'games', 'wins', 'losses', 'w_l_pct',
                  'playoffs', 'division', 'conference', 'championships', 'model_type')


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('player_name', 'position', 'age', 'team', 'games', 'games_started',
                  'minutes_played', 'field_goals', 'field_goals_attempted', 'field_goals_pct',
                  'three_pts', 'three_pts_attempted', 'three_pts_pct', 'two_pts', 'two_pts_attempted',
                  'two_pts_pct', 'effective_fg_pct', 'points', 'free_throws', 'free_throws_attempted',
                  'free_throws_pct', 'off_reb', 'def_reb', 'total_reb', 'assists', 'steals', 'blocks',
                  'turnovers', 'pers_fouls', 'model_type')
