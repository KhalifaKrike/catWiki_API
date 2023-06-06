from django.db import models
from django.core.validators import MaxValueValidator


class CatBreed(models.Model):
    image = models.URLField(max_length=200, blank=True)
    breed = models.CharField(max_length=100)
    description = models.TextField()
    temperament = models.CharField(max_length=150)
    origin = models.CharField(max_length=100)
    lifeSpan = models.CharField(max_length=100, blank=True)
    adaptability = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)], default=0)
    affectionLevel = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)], default=0)
    childFriendly = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)], default=0)
    grooming = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)], default=0)
    intelligence = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)], default=0)
    healthIssues = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)], default=0)
    socialNeeds = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)], default=0)
    strangerFriendly = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)], default=0)
    otherPhotos = models.TextField(blank=True)
    popularity = models.IntegerField(default=0)

    def __str__(self):
        return self.breed
