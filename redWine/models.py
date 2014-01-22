from django.db import models

class Bruker(models.Model):
    name = models.CharField(max_length=30)
    admin = models.BooleanField()
    totalWines = models.PositiveIntegerField()
    registered = models.DateTimeField()
    komite = models.CharField(max_length=30)

class Straff(models.Model):
    to = models.CharField(max_length=30)
    giver = models.CharField(max_length=30)
    amount = models.PositiveIntegerField()
    reason = models.CharField(max_length=80)
    date = models.DateTimeField(auto_now=True)
