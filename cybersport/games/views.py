from rest_framework import viewsets
from bll.Games_bll import GamesBLL
from .serializers import GamesSerializer


class GamesApiView(viewsets.ModelViewSet):
    serializer_class = GamesSerializer
    http_method_names = ['get']

    def get_queryset(self):
        games_bll = GamesBLL()
        return games_bll.fetch_all_games()
