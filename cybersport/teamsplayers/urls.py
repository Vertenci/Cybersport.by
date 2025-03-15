from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.main_features, name='teamsplayers'),
    path('teams', views.home_teams, name='teams'),
    path('players', views.home_players, name='players'),
    path('players/<int:pk>', views.PlayersDetailView.as_view(), name='detail_players'),
    path('teams/<int:pk>', views.TeamsDetailView.as_view(), name='detail_teams')
]
