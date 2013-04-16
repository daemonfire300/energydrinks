from django.http import HttpResponseRedirect
from django.contrib.auth.views import login as login_view
from drinks.forms import UserCreateForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from drinks.models import Profile, Drink, DrinkStats, DailyDrink
import datetime

@login_required(login_url='/member/login/')
def drinks(request):
    drinks = Drink.objects.all()
    return render(request, 'drinks/drinks.html', {"drinks": drinks})

@login_required(login_url='/member/login/')
def drink(request, drink_id):
    drink = Drink.objects.get(id=drink_id)
    return render(request, 'drinks/singledrink.html', {"drink": drink})

@login_required(login_url='/member/login/')
def mydrinks(request):
    drinks = DrinkStats.objects.filter(profile=request.user.profile)
    return render(request, 'drinks/mydrinks.html', {"drinks": drinks})

@login_required(login_url='/member/login/')
def adddrink(request, drink_id):
    drink = Drink.objects.get(id=drink_id)
    already_drank = DrinkStats.objects.filter(profile=request.user.profile, drink=drink)
    if already_drank.count() > 0:
        print "already"
    else:
        print "new"
        DrinkStats.objects.create(profile=request.user.profile, drink=drink)
        daily = DailyDrink.objects.get(profile=request.user.profile, date=datetime.date())
        if daily is not None:
            daily.volume += drink.volume
        else:
            DailyDrink.objects.create(profile=request.user.profile, volume=drink.volume)
    
    return HttpResponseRedirect('/mydrinks')

@login_required(login_url='/member/login/')
def inc_drink(request, drink_id):
    drink = Drink.objects.get(id=drink_id)
    drink_stats = DrinkStats.objects.get(profile=request.user.profile, drink=drink)
    if drink_stats:
        print "good"
        drink_stats.amount += 1
        drink_stats.save()
    else:
        print "new"
        DrinkStats.objects.create(profile=request.user.profile, drink=drink)
    
    daily = DailyDrink.objects.get(profile=request.user.profile, date=datetime.date())
    if daily is not None:
        daily.volume += drink.volume
    else:
        DailyDrink.objects.create(profile=request.user.profile, volume=drink.volume)
    
    return HttpResponseRedirect('/mydrinks')

@login_required(login_url='/member/login/')
def dec_drink(request, drink_id):
    drink = Drink.objects.get(id=drink_id)
    drink_stats = DrinkStats.objects.get(profile=request.user.profile, drink=drink)
    if drink_stats:
        print "good"
        if drink_stats.amount > 0:
            drink_stats.amount -= 1
            drink_stats.save()
    else:
        print "new"
        DrinkStats.objects.create(profile=request.user.profile, drink=drink)
    
    return HttpResponseRedirect('/mydrinks')

def member_login(request, template_name):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile')
    else:
        return login_view(request, template_name)

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            print new_user
            return HttpResponseRedirect("/profile")
    else:
        form = UserCreateForm()
    return render(request, 'member/register.html', {'form': form})

@login_required(login_url='/member/login/')
def profile(request, user_id):
    profile = Profile.objects.get(pk=user_id)
    return render(request, 'member/foreign_profile.html', {"profile": profile})

@login_required(login_url='/member/login/')
def index(request):
    profile = request.user.profile
    return render(request, 'member/member_profile.html', {"profile": profile})