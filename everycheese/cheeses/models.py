from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel
from slugify import slugify


class Cheese(TimeStampedModel):

    class Firmness(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        SOFT = "soft", "Soft"
        SEMI_SOFT = "semi-soft", "Semi-Soft"
        SEMI_HARD = "semi-hard", "Semi-Hard"
        HARD = "hard", "Hard"

    name = models.CharField(max_length=255)
    description = models.TextField("Description", blank=True)
    slug = models.SlugField("Cheese Address",
                            unique=True,
                            blank=True,
                            )
    firmness = models.CharField("Firmness", max_length=20, choices=Firmness.choices, default=Firmness.UNSPECIFIED)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Cheese, self).save(*args, **kwargs)
