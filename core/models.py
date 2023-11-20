from django.db import models
from attractions.models import Attraction
from comments.models import Comment
from ratings.models import Rating
from localizations.models import Localization

class TouristSpot(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attraction)
    comments = models.ManyToManyField(Comment)
    ratings = models.ManyToManyField(Rating)
    localization = models.ForeignKey(Localization, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name