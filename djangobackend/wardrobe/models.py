from django.db import models

# Create your models here.


class Clothes(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.CharField(max_length=1000, null=True)
    colour = models.CharField(max_length=64)  # options
    condition = models.CharField(max_length=64)  # options
    purchasedDate = models.DateTimeField()
