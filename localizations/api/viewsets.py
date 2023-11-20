from rest_framework.viewsets import ModelViewSet
from localizations.models import Localization
from .serializers import LocalizationSerializer

class LocalizationViewSet(ModelViewSet):
    queryset = Localization.objects.all()
    serializer_class = LocalizationSerializer