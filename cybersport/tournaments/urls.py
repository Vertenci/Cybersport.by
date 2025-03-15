from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.tour_home, name='tour_home'),
    path('<int:pk>', views.TournamentsDetailView.as_view(), name='detail_tour')
]
