from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic.base import RedirectView
admin.autodiscover()

urlpatterns = patterns('',

    # redirect to login page
    url(r'^$', RedirectView.as_view(url='/member/login/'), name='root'),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^drinks/$', 'drinks.views.drinks'),
    url(r'^drinks/stats/$', 'drinks.views.drinkstats'),
    url(r'^mydrinks/$', 'drinks.views.mydrinks'),
    url(r'^drinks/(?P<drink_id>\d+)/$', 'drinks.views.drink'),
    url(r'^drinks/add/(?P<drink_id>\d+)/$', 'drinks.views.adddrink'),
    url(r'^drinks/increase/(?P<drink_id>\d+)/$', 'drinks.views.inc_drink'),
    url(r'^drinks/decrease/(?P<drink_id>\d+)/$', 'drinks.views.dec_drink'),
    url(r'^member/login/$', 'drinks.views.member_login', {'template_name': 'member/login.html'}),
    url(r'^member/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/member/login/'}),
    # foreign profile
    url(r'^profile/(?P<user_id>\d+)/$', 'drinks.views.profile'),
    # own profile
    url(r'^profile/$', 'drinks.views.index'),
    url(r'^member/register/$', 'drinks.views.register'),
    #(r'^static/(?P<path>.*)$', 'django.views.static.serve'),
)
