from django.shortcuts import render
from django.views.generic import DetailView
from bll.Articles_bll import ArticleBLL
from .models import Articles
from bll.Games_bll import GamesBLL


def news_home(request):
    article_bll = ArticleBLL()
    gamesbll = GamesBLL()
    games = gamesbll.fetch_all_games()

    selected_game_id = request.GET.get('game_id')
    filter_type = request.GET.get('filter')

    if selected_game_id:
        articles = article_bll.fetch_article_by_game(selected_game_id)
    else:
        articles = article_bll.fetch_all_articles()

    context = {
        'games': games,
        'selected_game_id': int(selected_game_id) if selected_game_id else None,
        'filter_type': filter_type,
        'articles': articles
    }

    return render(request, 'news/news_home.html', context)


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/detail_news.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        bll = ArticleBLL()
        return bll.get_article(self.kwargs['pk'])
