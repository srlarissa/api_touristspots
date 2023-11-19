from django.db import models

class Localization(models.Model):
    first_line = models.CharField(max_length=150)
    second_line = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=100)
    estate = models.CharField(max_length=50)
    country = models.CharField(max_length=70)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.first_line