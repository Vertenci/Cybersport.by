from dal.repository_interface.IRepository import IRepository
from django.shortcuts import get_object_or_404
from games.models import Games


class GamesRepository(IRepository):
    def insert(self, entity):
        entity.save()

    def delete(self, entity_id):
        game = self.get(entity_id)
        if game:
            game.delete()

    def update(self, entity):
        entity.save()

    def get(self, entity_id):
        return get_object_or_404(Games, id=entity_id)

    def get_all(self):
        return list(Games.objects.all())
