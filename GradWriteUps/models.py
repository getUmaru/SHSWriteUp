from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class WriteUp(models.Model):
  username = models.SlugField(max_length=255, unique=True)
  yearbook = models.TextField(max_length=300)
  commencement = models.TextField(max_length=300)
  height_feet = models.CharField(max_length=1)
  commencement = models.CharField(max_length=2)

  class Meta:
  #ordering = ['-created]

    def __unicode__(self):
      return u'%s' % self.yearbook
  def get_absolute_url(self):
    return reverse('writeups.views.writeup', args=[self.username])
