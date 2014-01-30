from django.db import models

class Bruker(models.Model):
    name = models.CharField(max_length=30)
    admin = models.BooleanField(default=False)
    registered = models.DateTimeField(auto_now=True)
    komite = models.CharField(max_length=30, default='dotKom')
    def total(self):
        return sum([straff.amount for straff in self.straffer.all()])
    def __unicode__(self):
        return u'%s' % (self.name)

class Straff(models.Model):
    to = models.ForeignKey(Bruker, related_name='straffer')
    giver = models.ForeignKey(Bruker, related_name='straffer_gitt')
    amount = models.PositiveIntegerField()
    reason = models.CharField(max_length=80)
    date = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return u'%s - %s' % (self.amount, self.to)
