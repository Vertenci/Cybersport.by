from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('news.urls')),
    path('tournaments/', include('tournaments.urls')),
    path('matches/', include('matches.urls')),
    path('teamsplayers/', include('teamsplayers.urls')),
    path('profile/', include('userprofiles.urls')),
    path('', include('games.urls'))
]

