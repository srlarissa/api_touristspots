from django.db import models
from django.contrib.auth.models import User

class Rating(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username.username