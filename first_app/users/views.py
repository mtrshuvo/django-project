from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(req):
    print("hello")
    return HttpResponse("Hello world")