from django.conf.urls import url
from .views import adpan, index, login


urlpatterns = [
  url(r'^adminpanel/$', adpan, name="adpan"),
  url(r'^$', index, name="index"),
  url(r'^login/$', login, name="login"),
]
