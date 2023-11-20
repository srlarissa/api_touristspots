from rest_framework.serializers import ModelSerializer
from ratings.models import Rating

class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'username', 'comment', 'rating', 'date']