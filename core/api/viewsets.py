from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from core.models import TouristSpot
from .serializers import TouristSpotSerializer

class TouristSpotViewSet(ModelViewSet):
    serializer_class = TouristSpotSerializer
    filter_backends=[SearchFilter]
    search_fields=['name', 'description']

    def get_queryset(self):
       id = self.request.query_params.get('id', None)
       name = self.request.query_params.get('name', None)
       description = self.request.query_params.get('description', None)
       queryset = TouristSpot.objects.all()

       if id:
           queryset = TouristSpot.objects.filter(pk=id)

       if name:
           queryset = TouristSpot.objects.filter(name__iexact=name)

       if description:
           queryset = TouristSpot.objects.filter(description__iexact=description)

       return queryset

