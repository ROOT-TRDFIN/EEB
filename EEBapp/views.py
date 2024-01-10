from django.shortcuts import render
from operator import index
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def product(request):
    return render(request, 'our_products.html')

#Dome
def domeindex(request):
    return render(request, 'dome.html')

def domeabout(request):
    return render(request,'domabout.html')

def domeblog(request):
    return render(request,'domblog.html')

def domecontact(request):
    return render(request,'domcontact.html')

def domeservices(request):
    return render(request,'domservices.html')

#Autoplanter
def autoindex(request):
    return render(request,'autoplanter.html')

def autoabout(request):
    return render(request,'autoabout.html')

def autocontact(request):
    return render(request,'autocontact.html')

def autoportfolio(request):
    return render(request,'autoportfolio.html')

#Amphibious Cycle

def ampibious(request):
    return render(request,'ampibious.html')

#Floatation Tank
def floatation(request):
    return render(request,'floatation.html')

#Hydrophonics
def hydro(request):
    return render(request,'hydro.html')

#Scafolding
def scafolding(request):
    return render(request,'scafolding.html')
