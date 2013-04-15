from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os

class Drink(models.Model):
    name = models.CharField(max_length=128, default="unknown drink")
    volume = models.IntegerField(default=0)
    caffeine = models.IntegerField(default=0)
    image = models.ImageField(upload_to=os.path.join(os.path.dirname(__file__), '../static/images').replace('\\','/'))
    #image = models.ImageField(upload_to="/home/dotcloud/data/media/")
    
    def __unicode__(self):
        return "%s %s ml %s mg" % (self.name, self.volume, self.caffeine)

class Profile(models.Model):
    user = models.OneToOneField(User)
    drinks = models.ManyToManyField(Drink, through="DrinkStats")
    
class DrinkStats(models.Model):
    profile = models.ForeignKey(Profile)
    drink = models.ForeignKey(Drink)
    amount = models.IntegerField(default=1)
    last_time = models.DateTimeField(auto_now_add=True)