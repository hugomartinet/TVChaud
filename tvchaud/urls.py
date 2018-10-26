"""tvchaud URL Configuration

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
from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LoginView

import series.views as series
from . import views

app_name = 'tvchaud'

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='series/home'), name='home'),

    url(r'^admin/', admin.site.urls),

    url(r'^login/', LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/', views.mylogout, name='logout'),
    url(r'^register/', views.register, name='register'),
    url(r'^auth/', include('social_django.urls', namespace='social')),

    url(r'^series/', include('series.urls')),
    url(r'^user/', include('user.urls')),
]
