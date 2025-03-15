from news.models import Articles
from dal.repository_interface.IRepository import IRepository
from django.shortcuts import get_object_or_404


class ArticleRepository(IRepository):
    def insert(self, entity):
        entity.save()

    def delete(self, entity_id):
        article = self.get(entity_id)
        if article:
            article.delete()

    def update(self, entity):
        entity.save()

    def get(self, entity_id):
        return get_object_or_404(Articles, id=entity_id)

    def get_all(self):
        return list(Articles.objects.all().order_by('-date'))

    def get_article_by_game(self, game_id):
        return list(Articles.objects.filter(game_id=game_id))
