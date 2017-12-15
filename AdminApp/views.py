from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import WriteUp
#from django.core.context_processors import csrf

# Create your views here.
def index(request):
  writeups = WriteUp.objects.all()
  return render(request,'index.html', {'writeups': writeups})
  #return HttpResponse ("<h1>Hello World!</h1>")

def login(request):
  return render(request, 'login.html', {})
 
def adpan(request):
  print("Hey, Welcome to Admin Panel")
  return render(request, 'adpan.html')
  #return HttpResponse ("<h1>Hello World!</h1>")
