from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def render_home(request):
    return HttpResponse('Home page')

def render_room(request):
    return HttpResponse('Room')