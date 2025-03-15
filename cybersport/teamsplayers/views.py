from django.shortcuts import render
from bll.Games_bll import GamesBLL
from bll.Teams_bll import TeamsBLL
from bll.Players_bll import PlayersBLL
from django.views.generic import DetailView
from players.models import Players, PlayerTeamHistory
from teams.models import Teams


def main_features(request):
    return render(request, 'teamsplayers/layout_teamsplayers.html')


def home_teams(request):
    gamesbll = GamesBLL()
    games = gamesbll.fetch_all_games()
    teamsbll = TeamsBLL()

    selected_game_id = request.GET.get('game_id')
    filter_type = request.GET.get('filter')

    if selected_game_id:
        teams = teamsbll.fetch_teams_by_game(selected_game_id)
    else:
        teams = teamsbll.fetch_all_teams()

    for team in teams:
        indicators = team.indicators
        team.total_matches = indicators.wins + indicators.loses + indicators.draws
        team.win_percent = (indicators.wins / team.total_matches * 100) if team.total_matches > 0 else 0
        team.lose_percent = (indicators.loses / team.total_matches * 100) if team.total_matches > 0 else 0
        team.draw_percent = (indicators.draws / team.total_matches * 100) if team.total_matches > 0 else 0

    teams.sort(key=lambda x: x.win_percent, reverse=True)

    context = {
        'games': games,
        'teams': teams,
        'selected_game_id': int(selected_game_id) if selected_game_id else None,
        'filter_type': filter_type,
    }

    return render(request, 'teamsplayers/teams_page.html', context)


def home_players(request):
    gamesbll = GamesBLL()
    games = gamesbll.fetch_all_games()
    playersbll = PlayersBLL()

    selected_game_id = request.GET.get('game_id')
    filter_type = request.GET.get('filter')

    if selected_game_id:
        players = playersbll.fetch_players_by_game(selected_game_id)
    else:
        players = playersbll.fetch_all_players()

    for player in players:
        player.total_matches = player.wins + player.loses + player.draws
        player.win_percent = (player.wins / player.total_matches * 100) if player.total_matches > 0 else 0
        player.lose_percent = (player.loses / player.total_matches * 100) if player.total_matches > 0 else 0
        player.draw_percent = (player.draws / player.total_matches * 100) if player.total_matches > 0 else 0

    players.sort(key=lambda x: x.sum_prize, reverse=True)

    context = {
        'games': games,
        'players': players,
        'selected_game_id': int(selected_game_id) if selected_game_id else None,
        'filter_type': filter_type,
    }

    return render(request, 'teamsplayers/players_page.html', context)


class PlayersDetailView(DetailView):
    model = Players
    template_name = 'teamsplayers/detail_player.html'
    context_object_name = 'player'

    def get_object(self, queryset=None):
        bll = PlayersBLL()
        player = bll.get_player(self.kwargs['pk'])

        player.total_matches = player.wins + player.loses + player.draws
        player.win_percent = (player.wins / player.total_matches * 100) if player.total_matches > 0 else 0
        player.lose_percent = (player.loses / player.total_matches * 100) if player.total_matches > 0 else 0
        player.draw_percent = (player.draws / player.total_matches * 100) if player.total_matches > 0 else 0

        return player


class TeamsDetailView(DetailView):
    model = Teams
    template_name = 'teamsplayers/detail_team.html'
    context_object_name = 'team'

    def get_object(self, queryset=None):
        bll = TeamsBLL()
        team = bll.get_team(self.kwargs['pk'])

        team.total_matches = team.indicators.wins + team.indicators.loses + team.indicators.draws
        team.win_percent = (team.indicators.wins / team.total_matches * 100) if team.total_matches > 0 else 0
        team.lose_percent = (team.indicators.loses / team.total_matches * 100) if team.total_matches > 0 else 0
        team.draw_percent = (team.indicators.draws / team.total_matches * 100) if team.total_matches > 0 else 0

        players = team.players.all()

        team.player_stats = {}

        for player in players:
            player.total_matches = player.wins + player.loses + player.draws
            player.win_percent = (player.wins / player.total_matches * 100) if player.total_matches > 0 else 0
            player.lose_percent = (player.loses / player.total_matches * 100) if player.total_matches > 0 else 0
            player.draw_percent = (player.draws / player.total_matches * 100) if player.total_matches > 0 else 0

            team.player_stats[player.id] = {
                'total_matches': player.total_matches,
                'win_percent': player.win_percent,
                'lose_percent': player.lose_percent,
                'draw_percent': player.draw_percent,
                'wins': player.wins,
                'draws': player.draws,
                'loses': player.loses,
            }

        player_history = {
            player.id: PlayerTeamHistory.objects.filter(player=player, team=team).first()
            for player in players
        }

        team.player_history = player_history

        return team
