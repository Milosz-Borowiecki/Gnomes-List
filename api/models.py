from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator,MinValueValidator

class Gnome(models.Model):

    class Races(models.TextChoices):
        ROCK = 'Rock',_('Rock')
        SKY = 'Sky',_('Sky')
        FOREST = 'Forest',_('Forest')
        FIRE = 'Fire',_('Fire')
        RIVER = 'River',_('River')

    race = models.CharField(
        max_length=6,
        choices=Races.choices,
        default=Races.FOREST,
    )

    name = models.TextField(max_length=35)
    age = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    strength = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(150),
            MinValueValidator(1)
        ]
    )
    avatar = models.ImageField()

    def __str__(self):
        return self.name