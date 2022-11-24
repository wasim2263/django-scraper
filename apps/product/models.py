import jsonfield
from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel


class Category(SoftDeletableModel, TimeStampedModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(SoftDeletableModel, TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    currency = models.CharField(max_length=50)
    summary = jsonfield.JSONField()

    class Meta:
        indexes = [
            models.Index(fields=['title']),
        ]

    def __str__(self):
        return self.title
