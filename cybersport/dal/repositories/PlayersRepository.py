from django.shortcuts import get_object_or_404
from dal.repository_interface.IRepository import IRepository
from players.models import Players


class PlayersRepository(IRepository):
    def insert(self, entity):
        entity.save()

    def delete(self, entity_id):
        player = self.get(entity_id)
        if player:
            player.delete()

    def update(self, entity):
        entity.save()

    def get(self, entity_id):
        return get_object_or_404(Players, id=entity_id)

    def get_all(self):
        return list(Players.objects.all())

    def get_players_by_game(self, game_id):
        return list(Players.objects.filter(game_id=game_id))
