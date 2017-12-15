from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from .models import WriteUp

# Create your views here.

def credits(request):
  return render(request, 'credits.html', {})


def writeups(request, username):
  print(username)
  return render_to_repsonse('writeup.html', {
    'writeup': get_object_or_404(WriteUp, username=username)})
    


