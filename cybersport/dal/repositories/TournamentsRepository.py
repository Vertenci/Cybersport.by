from dal.repository_interface.IRepository import IRepository
from django.shortcuts import get_object_or_404

from tournaments.models import Tournaments


class TournamentsRepository(IRepository):
    def insert(self, entity):
        entity.save()

    def delete(self, entity_id):
        tournament = self.get(entity_id)
        if tournament:
            tournament.delete()

    def update(self, entity):
        entity.save()

    def get(self, entity_id):
        return get_object_or_404(Tournaments, id=entity_id)

    def get_all(self):
        return list(Tournaments.objects.all())
