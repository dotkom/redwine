from django.db import models

class Bruker(models.Model):
    name = models.CharField(max_length=30)
    admin = models.BooleanField(default=False)
    totalWines = models.PositiveIntegerField(default=0)
    registered = models.DateTimeField(auto_now=True)
    komite = models.CharField(max_length=30, default='dotKom')

class Straff(models.Model):
    to = models.CharField(max_length=30)
    giver = models.CharField(max_length=30)
    amount = models.PositiveIntegerField()
    reason = models.CharField(max_length=80)
    date = models.DateTimeField(auto_now=True)
