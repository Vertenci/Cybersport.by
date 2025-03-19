from django.urls import path, include
from . import views
from rest_framework import routers
from .views import MatchesApiView

router = routers.DefaultRouter()
router.register(r'api/matches', MatchesApiView, basename='matches')

urlpatterns = [
    path('', views.match_home, name='home-matches'),
    path('<int:pk>/', views.MatchesDetailView.as_view(), name='detail_match'),
    path('', include(router.urls))
]
