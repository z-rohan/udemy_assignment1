from django.db import models

# Create your models here.

class Passengers(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    travel_points = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.fname} {self.lname} {self.travel_points}"