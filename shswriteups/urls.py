"""shswriteups URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from GradWriteUps.views import writeups, credits
from GradWriteUps import views 
from django.contrib.auth.views import login, logout
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^gwp/', include('GradWriteUps.urls')),
    url(r'^cu/', include('CustomUser.urls')),
    url(r'^aa/', include('AdminApp.urls')),
    url(r'^logout/$', logout, name="logout"),
    url(r'^admin/', admin.site.urls, name="admin"),
    url(r'^$', RedirectView.as_view(url='/aa/')),
  
    ## STUNDENT APP AUTHENTICATION ROUTES ##
    #url(r'^login/$', login {'template_name': 'login.html'}, name="login"),
    #url(r'^$', index, name="index"),
    #url(r'^login/$', views.login, name='login'),
    #url(r'^adminpan/$', views.adminpan, name="adminpan")
    ## END STUNDENT APP AUTHENTICATION ROUTES ##
]
