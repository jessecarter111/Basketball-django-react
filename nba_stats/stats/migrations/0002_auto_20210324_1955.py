# Generated by Django 3.1.7 on 2021-03-24 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Franchise',
            fields=[
                ('franchise_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('franchise_name', models.CharField(max_length=50)),
                ('league', models.CharField(max_length=8)),
                ('inaug', models.CharField(max_length=7)),
                ('end', models.CharField(max_length=7)),
                ('years', models.IntegerField()),
                ('games', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('w_l_pct', models.DecimalField(decimal_places=1, max_digits=3)),
                ('playoffs', models.IntegerField()),
                ('division', models.IntegerField()),
                ('conference', models.IntegerField()),
                ('championships', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='player',
            name='age',
        ),
        migrations.RemoveField(
            model_name='player',
            name='assists',
        ),
        migrations.RemoveField(
            model_name='player',
            name='blocks',
        ),
        migrations.RemoveField(
            model_name='player',
            name='def_reb',
        ),
        migrations.RemoveField(
            model_name='player',
            name='effective_fg_pct',
        ),
        migrations.RemoveField(
            model_name='player',
            name='field_goals',
        ),
        migrations.RemoveField(
            model_name='player',
            name='field_goals_attempted',
        ),
        migrations.RemoveField(
            model_name='player',
            name='field_goals_pct',
        ),
        migrations.RemoveField(
            model_name='player',
            name='free_throws',
        ),
        migrations.RemoveField(
            model_name='player',
            name='free_throws_attempted',
        ),
        migrations.RemoveField(
            model_name='player',
            name='free_throws_pct',
        ),
        migrations.RemoveField(
            model_name='player',
            name='games',
        ),
        migrations.RemoveField(
            model_name='player',
            name='games_started',
        ),
        migrations.RemoveField(
            model_name='player',
            name='id',
        ),
        migrations.RemoveField(
            model_name='player',
            name='minutes_played',
        ),
        migrations.RemoveField(
            model_name='player',
            name='off_reb',
        ),
        migrations.RemoveField(
            model_name='player',
            name='pers_fouls',
        ),
        migrations.RemoveField(
            model_name='player',
            name='points',
        ),
        migrations.RemoveField(
            model_name='player',
            name='steals',
        ),
        migrations.RemoveField(
            model_name='player',
            name='team',
        ),
        migrations.RemoveField(
            model_name='player',
            name='three_pts',
        ),
        migrations.RemoveField(
            model_name='player',
            name='three_pts_attempted',
        ),
        migrations.RemoveField(
            model_name='player',
            name='three_pts_pct',
        ),
        migrations.RemoveField(
            model_name='player',
            name='total_reb',
        ),
        migrations.RemoveField(
            model_name='player',
            name='turnovers',
        ),
        migrations.RemoveField(
            model_name='player',
            name='two_pts',
        ),
        migrations.RemoveField(
            model_name='player',
            name='two_pts_attempted',
        ),
        migrations.RemoveField(
            model_name='player',
            name='two_pts_pct',
        ),
        migrations.RemoveField(
            model_name='team',
            name='championships',
        ),
        migrations.RemoveField(
            model_name='team',
            name='conference',
        ),
        migrations.RemoveField(
            model_name='team',
            name='division',
        ),
        migrations.RemoveField(
            model_name='team',
            name='end',
        ),
        migrations.RemoveField(
            model_name='team',
            name='games',
        ),
        migrations.RemoveField(
            model_name='team',
            name='id',
        ),
        migrations.RemoveField(
            model_name='team',
            name='inaug',
        ),
        migrations.RemoveField(
            model_name='team',
            name='team_abrev',
        ),
        migrations.RemoveField(
            model_name='team',
            name='years',
        ),
        migrations.AddField(
            model_name='player',
            name='birth_date',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='player',
            name='draft_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='end_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='height',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='player_id',
            field=models.CharField(default='0', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='player',
            name='weight',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='coaches',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='drtg',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='finish',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='ortg',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='pace',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='relative_drtg',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='relative_ortg',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='relative_pace',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='season',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='srs',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='team_id',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='team',
            name='top_ws',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='league',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='losses',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='playoffs',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='w_l_pct',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='wins',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Player_Game',
            fields=[
                ('season', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('age', models.IntegerField()),
                ('league', models.CharField(max_length=4)),
                ('position', models.CharField(max_length=5)),
                ('games', models.IntegerField()),
                ('games_started', models.IntegerField()),
                ('minutes_played', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('field_goals', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('field_goals_attempted', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('field_goals_pct', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('three_pts', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('three_pts_attempted', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('three_pts_pct', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('two_pts', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('two_pts_attempted', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('two_pts_pct', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('effective_fg_pct', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('free_throws', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('free_throws_attempted', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('free_throws_pct', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('off_reb', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('def_reb', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('total_reb', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('assists', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('steals', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('blocks', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('turnovers', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('pers_fouls', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('points', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('model_type', models.CharField(default='player_stats', max_length=50)),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.team')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='franchise_id',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, to='stats.franchise'),
        ),
    ]
