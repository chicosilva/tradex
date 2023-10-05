from django.db import models
from model_utils.managers import QueryManager

from apps.shared.models import ModelDefault


class Product(ModelDefault):

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    ean = models.CharField(max_length=13, unique=True)
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_price = models.DecimalField(max_digits=10, decimal_places=2)
    objects = QueryManager(canceled_at__isnull=True)

    def __str__(self):
        return self.name


class PriceVariation(ModelDefault):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='pricevariations')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.product.name}- {self.start_date} - {self.end_date}"
