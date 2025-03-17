from rest_framework import routers
from .views import GamesApiView

router = routers.DefaultRouter()
router.register(r'api/games', GamesApiView, basename='games')

urlpatterns = router.urls
