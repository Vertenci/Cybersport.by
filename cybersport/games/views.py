from rest_framework import viewsets, status
from bll.Games_bll import GamesBLL
from rest_framework.response import Response
from .serializers import GamesSerializer


class GamesApiView(viewsets.ModelViewSet):
    serializer_class = GamesSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    class Meta:
        tags = ['Games']

    def get_queryset(self):
        games_bll = GamesBLL()
        return games_bll.fetch_all_games()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            game = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        games_bll = GamesBLL()
        partial = kwargs.pop('partial', False)
        game_instance = games_bll.get_game(kwargs['pk'])
        if game_instance:
            serializer = self.get_serializer(game_instance, data=request.data, partial=partial)
            if serializer.is_valid():
                game = serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        games_bll = GamesBLL()
        game_instance = games_bll.get_game(kwargs['pk'])
        if game_instance:
            games_bll.delete_game(game_instance.id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, *args, **kwargs):
        games_bll = GamesBLL()
        game = games_bll.get_game(kwargs['pk'])
        if game:
            serializer = self.get_serializer(game)
            return Response(serializer.data)
        return Response({"detail": "Not found."}, status=404)
