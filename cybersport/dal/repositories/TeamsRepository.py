from dal.repository_interface.IRepository import IRepository
from django.shortcuts import get_object_or_404
from teams.models import Teams


class TeamsRepository(IRepository):
    def insert(self, entity):
        entity.save()

    def delete(self, entity_id):
        team = self.get(entity_id)
        if team:
            team.delete()

    def update(self, entity):
        entity.save()

    def get(self, entity_id):
        return get_object_or_404(Teams, id=entity_id)
    
    def get_all(self):
        return list(Teams.objects.all())

    def get_teams_by_game(self, game_id):
        return list(Teams.objects.filter(game_id=game_id))
