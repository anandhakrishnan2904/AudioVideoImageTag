from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def imageaudiovideo( request):
    return  render (request,"imageaudiovideo.html")