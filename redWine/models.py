from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
from django.db.models.signals import post_save

class UserProfile(models.Model):  
    user = models.OneToOneField(User)  
    komite = models.CharField(max_length=30, default='dotKom')
    def total(self):
        return sum([straff.amount for straff in self.straffer.all()])
    def __unicode__(self):
        return u'%s' % (self.user)

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 

class Straff(models.Model):
    to = models.ForeignKey(UserProfile, related_name='straffer')
    giver = models.ForeignKey(UserProfile, related_name='straffer_gitt')
    amount = models.PositiveIntegerField()
    reason = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return u'%s - %s' % (self.amount, self.to)
    class Meta:
        ordering = ['-date']
        get_latest_by = 'date'
