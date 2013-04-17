from django.contrib import admin
from drinks.models import Drink, DrinkStats, Profile, DailyDrink, Datasheet

admin.site.register(Drink)
admin.site.register(DrinkStats)
admin.site.register(Profile)
admin.site.register(DailyDrink)
admin.site.register(Datasheet)