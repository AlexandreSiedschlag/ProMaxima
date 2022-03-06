from django.http import HttpResponse
from django.shortcuts import redirect, render
from .functions import do_something

def home(response):
    return render(response, 'app1/home.html')

def index(response):
    do_something()
    return HttpResponse(response, 'http://127.0.0.1:8000/')
# Create your views here.
