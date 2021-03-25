from rest_framework import serializers
from .models import Franchise, Player, Team


class FranchiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Franchise
        fields = ('franchise_id', 'franchise_name', 'league', 'inaug',
                  'end', 'years', 'games', 'wins', 'losses', 'w_l_pct',
                  'playoffs', 'division', 'conference', 'championships')


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('player_id', 'player_name', 'draft_year', 'end_year',
                  'position', 'height', 'weight', 'birth_date')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('franchise_id', 'team_id', 'season', 'league',
                  'team_name', 'wins', 'losses', 'w_l_pct',
                  'finish', 'srs', 'pace', 'relative_pace',
                  'ortg', 'relative_ortg', 'drtg',
                  'relative_drtg', 'playoffs', 'coaches',
                  'top_ws')


# class PlayerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Player
#         fields = ('player_name', 'position', 'age', 'team', 'games', 'games_started',
#                   'minutes_played', 'field_goals', 'field_goals_attempted', 'field_goals_pct',
#                   'three_pts', 'three_pts_attempted', 'three_pts_pct', 'two_pts', 'two_pts_attempted',
#                   'two_pts_pct', 'effective_fg_pct', 'points', 'free_throws', 'free_throws_attempted',
#                   'free_throws_pct', 'off_reb', 'def_reb', 'total_reb', 'assists', 'steals', 'blocks',
#                   'turnovers', 'pers_fouls', 'model_type')
