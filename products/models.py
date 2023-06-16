from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock=models.IntegerField()
    image_url=models.CharField(max_length=2890)


class Offer(models.Model):
    code = models.CharField(max_length=255)
    desciption = models.CharField(max_length=522)
    discount = models.FloatField()


