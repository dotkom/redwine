from django.db import models

class Bruker(models.Model):
    name = models.CharField(max_length=30)
    admin = models.CharField(max_length=50)
    totalWines = models.CharField(max_length=60)

class Straff(models.Model):
    to = models.CharField(max_length=30)
    giver = models.CharField(max_length=50)
    amount = models.CharField(max_length=60)
    reason = models.CharField(max_length=30)
    date = models.DateField()
