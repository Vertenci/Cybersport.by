from django.urls import path, include
from . import views


urlpatterns = [
    path('home-matches/', views.match_home, name='home-matches'),
    path('<int:pk>/', views.MatchesDetailView.as_view(), name='detail_match')
]
