from rest_framework.serializers import ModelSerializer
from core.models import TouristSpot
from attractions.api.serializers import AttractionSerializer
from localizations.api.serializers import LocalizationSerializer
from comments.api.serializers import CommentSerializer
from ratings.api.serializers import RatingSerializer

class TouristSpotSerializer(ModelSerializer):
    attractions = AttractionSerializer(many=True, read_only=True)
    localization = LocalizationSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    class Meta:
        model = TouristSpot
        fields = ['id', 'name', 'description', 'photo', 'attractions', 'localization', 'comments', 'ratings']