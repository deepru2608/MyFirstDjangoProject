from django.db import models


# Create your models here.


class Destination(models.Model):
    LocationName = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='pics')
    Description = models.TextField()
    Price = models.IntegerField()
    Offer = models.BooleanField(default=False)
