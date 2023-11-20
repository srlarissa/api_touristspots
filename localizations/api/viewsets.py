from rest_framework.viewsets import ModelViewSet
from localizations.models import Localization
from .serializers import LocalizationSerializer

class LocalizationsViewSet(ModelViewSet):
    queryset = Localization.objects.all()
    serializer_class = LocalizationSerializer