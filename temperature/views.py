from rest_framework import viewsets
from .models import Weather
from .serializers import WeatherSerializer
# Create your views here.
class WeatherListViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer