import jsonfield
from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel


class Source(SoftDeletableModel, TimeStampedModel):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=500, unique=True)
    category_selector = models.CharField(max_length=500)
    subcategory_selector = models.CharField(max_length=500)
    subcategory_selector = models.CharField(max_length=500)
    title_selector = models.CharField(max_length=500)
    price_selector = models.CharField(max_length=500)
    currency_selector = models.CharField(max_length=500)
    summary_selector = models.CharField(max_length=500)

    def __str__(self):
        return self.name

