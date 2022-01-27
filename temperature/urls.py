from .views import WeatherListViewSet
from rest_framework import routers


router=routers.SimpleRouter()
router.register(r'harorat',WeatherListViewSet)


urlpatterns = router.urls 
