from dal.repositories.ArticleRepository import ArticleRepository


class ArticleBLL:
    def __init__(self):
        self.article_dal = ArticleRepository()

    def fetch_all_articles(self):
        return self.article_dal.get_all()

    def create_article(self, form):
        self.article_dal.insert(form.save())

    def delete_article(self, article_id):
        self.article_dal.delete(article_id)

    def get_article(self, article_id):
        return self.article_dal.get(article_id)

    def update_article(self, article):
        return self.article_dal.update(article)

    def fetch_article_by_game(self, game_id):
        return self.article_dal.get_article_by_game(game_id)
