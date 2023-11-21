from rest_framework.viewsets import ModelViewSet
from core.models import TouristSpot
from .serializers import TouristSpotSerializer

class TouristSpotViewSet(ModelViewSet):
    serializer_class = TouristSpotSerializer

    def get_queryset(self):
       return TouristSpot.objects.filter(approved=True)