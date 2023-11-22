from django.db import models

class Attraction(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    business_hours = models.TextField()
    min_age = models.IntegerField()
    photo = models.ImageField(upload_to='attraction', blank=True, null=True)

    def __str__(self):
        return self.name