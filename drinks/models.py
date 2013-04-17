from django.db import models
from django.contrib.auth.models import User
import os

class Datasheet(models.Model):
    vitamin_a = models.IntegerField(default=1)
    vitamin_b = models.IntegerField(default=1)
    vitamin_c = models.IntegerField(default=1)
    vitamin_d = models.IntegerField(default=1)
    vitamin_b2 = models.IntegerField(default=1)
    vitamin_e = models.IntegerField(default=1)
    vitamin_b12 = models.IntegerField(default=1)
    vitamin_k = models.IntegerField(default=1)
    vitamin_b5 = models.IntegerField(default=1)
    vitamin_b7 = models.IntegerField(default=1)
    vitamin_b6 = models.IntegerField(default=1)
    vitamin_b3 = models.IntegerField(default=1)
    vitamin_b9 = models.IntegerField(default=1)
    calories = models.IntegerField(default=1)
    proteins = models.IntegerField(default=1)
    sugar = models.IntegerField(default=1)
    fat = models.IntegerField(default=0)
    carbohydrate = models.IntegerField(default=1)

class Drink(models.Model):
    name = models.CharField(max_length=128, default="unknown drink")
    datasheet = models.OneToOneField(Datasheet, null=True)
    volume = models.IntegerField(default=0)
    caffeine = models.IntegerField(default=0)
    image = models.ImageField(upload_to=os.path.join(os.path.dirname(__file__), '../static/images').replace('\\','/'))
    #image = models.ImageField(upload_to="/home/dotcloud/data/media/")
    
    def __unicode__(self):
        return "%s %s ml %s mg" % (self.name, self.volume, self.caffeine)
    @property
    def liter(self):
        return self.volume/1000
    
class Profile(models.Model):
    user = models.OneToOneField(User)
    drinks = models.ManyToManyField(Drink, through="DrinkStats")
    
class DrinkStats(models.Model):
    profile = models.ForeignKey(Profile)
    drink = models.ForeignKey(Drink)
    amount = models.IntegerField(default=1)
    last_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    
class DailyDrink(models.Model):
    profile = models.ForeignKey(Profile)
    volume = models.IntegerField(default=1)
    date = models.DateField(auto_now_add=True)
    
    @property
    def liter(self):
        return self.volume/1000