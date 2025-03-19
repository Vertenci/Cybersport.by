from datetime import date
from django.shortcuts import render
from django.views.generic import DetailView
from bll.Matches_bll import MatchesBLL
from bll.Games_bll import GamesBLL
from rest_framework.response import Response
from .models import Matches
from django.http import JsonResponse
from rest_framework import viewsets, status
from .serializers import MatchesSerializer


def match_home(request):
    match_bll = MatchesBLL()
    games_bll = GamesBLL()

    games = games_bll.fetch_all_games()
    selected_game_id = request.GET.get('game_id')
    filter_type = request.GET.get('filter')
    limit = int(request.GET.get('limit', 10))
    offset = int(request.GET.get('offset', 0))

    if selected_game_id:
        matches = match_bll.fetch_matches_by_game(selected_game_id)
    else:
        matches = match_bll.fetch_all_matches()

    today = date.today()
    if filter_type == "past":
        matches = [match for match in matches if match.date.date() < today]
    elif filter_type == "live":
        matches = [match for match in matches if match.date.date() == today]
    elif filter_type == "future":
        matches = [match for match in matches if match.date.date() > today]

    total_matches = len(matches)
    matches = matches[offset:offset + limit]

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'matches': [{
                'id': match.id,
                'date': match.date.strftime('%H:%M'),
                'game_icon': match.game.icon.url,
                'team_one_icon': match.team_one.icon.url,
                'team_one_name': match.team_one.name,
                'team_two_icon': match.team_two.icon.url,
                'team_two_name': match.team_two.name,
                'score': match.score if match.date.date() < today else 'vs',
                'tournament': match.tournament.name,
            } for match in matches],
            'has_more': offset + limit < total_matches,
        })

    context = {
        'matches': matches,
        'games': games,
        'selected_game_id': int(selected_game_id) if selected_game_id is not None else None,
        'filter_type': filter_type,
        'today': today,
        'has_more': limit < total_matches,
    }

    return render(request, 'matches/main_match.html', context)


class MatchesDetailView(DetailView):
    model = Matches
    template_name = 'matches/detail_match.html'
    context_object_name = 'match'

    def get_object(self, queryset=None):
        bll = MatchesBLL()
        return bll.get_match(self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = date.today()
        return context


class MatchesApiView(viewsets.ModelViewSet):
    serializer_class = MatchesSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    class Meta:
        tags = ['Matches']

    def get_queryset(self):
        matches_bll = MatchesBLL()
        return matches_bll.fetch_all_matches()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            match = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        matches_bll = MatchesBLL()
        match_instance = matches_bll.get_match(kwargs['pk'])
        if match_instance:
            matches_bll.delete_match(match_instance.id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        matches_bll = MatchesBLL()
        partial = kwargs.pop('partial', False)
        match_instance = matches_bll.get_match(kwargs['pk'])
        if match_instance:
            serializer = self.get_serializer(match_instance, data=request.data, partial=partial)
            if serializer.is_valid():
                match = serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, *args, **kwargs):
        matches_bll = MatchesBLL()
        match = matches_bll.get_match(kwargs['pk'])
        if match:
            serializer = self.get_serializer(match)
            return Response(serializer.data)
        return Response({"detail": "Not found."}, status=404)
