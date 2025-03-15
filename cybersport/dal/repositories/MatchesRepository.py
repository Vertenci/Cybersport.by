from dal.repository_interface.IRepository import IRepository
from django.shortcuts import get_object_or_404
from matches.models import Matches


class MatchesRepository(IRepository):
    def insert(self, entity):
        entity.save()

    def delete(self, entity_id):
        match = self.get(entity_id)
        if match:
            match.delete()

    def update(self, entity):
        entity.save()

    def get(self, entity_id):
        return get_object_or_404(Matches, id=entity_id)

    def get_all(self):
        return list(Matches.objects.all())

    def get_matches_by_game(self, game_id):
        return list(Matches.objects.filter(game_id=game_id))