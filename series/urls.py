"""series URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views

app_name = 'series'

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='home'),  name='home'),
    url(r'^home', views.home, name='home'),
    url(r'^details/(?P<tv_id>[0-9]+)/$', views.series_details, name='details'),
    url(r'^details/(?P<tv_id>[0-9]+)/(?P<season_number>[0-9]+)/$', views.season_details, name='season_details'),

    # ajax calls
    url(r'^ajax/see_notif/$', views.ajax_see_notif, name='ajax_see_notif'),
    url(r'^ajax/check_notif/$', views.ajax_check_notif, name='ajax_check_notif'),
]
