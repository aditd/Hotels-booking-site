from django.db import models
from django.db.models.base import Model
from django.db.models.fields import IntegerField
import numpy as np
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Hotel(models.Model):
    name        = models.CharField(max_length=100)
    price       = models.IntegerField()
    address     = models.CharField(max_length=100)
    longitude   = models.FloatField()
    latitude    = models.FloatField()
    smoking_rooms=models.BooleanField(default=False)
    pool        = models.BooleanField(default=False)
    gym         = models.BooleanField(default=False)
    room_service= models.BooleanField(default=False)
    spa         = models.BooleanField(default=False)
    breakfast   = models.BooleanField(default=False)
    free_wifi   = models.BooleanField(default=False)
    dry_cleaning= models.BooleanField(default=False)


    class Meta:
        ordering = ['name']

    def average_rating():
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return f"/hotels/{self.id}"

    def __str__(self):
        return self.name

class Photo(models.Model):
    url     = models.CharField(max_length=400)
    hotel   = models.ForeignKey(Hotel, on_delete=models.CASCADE)


class Review(models.Model):
    #writer  = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel   = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    rating  = models.IntegerField(default=3,validators=[MinValueValidator(0), MaxValueValidator(5)])