from django.shortcuts import get_object_or_404

from dal.repository_interface.IRepository import IRepository
from indicators.models import Indicators


class IndicatorsRepository(IRepository):
    def insert(self, entity):
        entity.save()

    def delete(self, entity_id):
        indicator = self.get(entity_id)
        if indicator:
            indicator.save()

    def update(self, entity):
        entity.save()

    def get(self, entity_id):
        return get_object_or_404(Indicators, id=entity_id)

    def get_all(self):
        return list(Indicators.objects.all())
