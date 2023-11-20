from rest_framework.serializers import ModelSerializer
from localizations.models import Localization

class LocalizationSerializer(ModelSerializer):
    class Meta:
        model = Localization
        fields = ('id', 'first_line', 'second_line', 'city', 'estate', 'country')