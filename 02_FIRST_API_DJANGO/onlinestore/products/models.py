from django.db import models


# Create your models here.

class Manifacturer(models.Model):

    name = models.CharField(max_length=140)

    location = models.CharField(max_length=140)

    active = models.BooleanField(default=True)


    def __str__(self):
        return self.name


class Product(models.Model):

    manifacturer = models.ForeignKey(Manifacturer,

                                     on_delete=models.CASCADE,

                                     related_name='products')

    name = models.CharField(max_length=140)

    description = models.TextField(blank=True, null=True)

    photo = models.ImageField(upload_to='products', blank=True, null=True)

    price = models.FloatField()

    shipping_cost = models.FloatField()

    quantity = models.PositiveSmallIntegerField()


    def __str__(self):
        return self.name