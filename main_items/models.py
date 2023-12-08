from django.db import models
from django.core.validators import MinValueValidator

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.IntegerField(null=False,blank=False,validators=[MinValueValidator(0)])

    def __str__(self):
        return (f'{self.name} {self.description} {self.price}')
