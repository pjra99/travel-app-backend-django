from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def location(request):
     return HttpResponse("This is the location page")