from django.http import HttpResponse
from django.shortcuts import render
from .functions import do_something

def home(response):
    return render(response, 'app1/home.html')

def index(response):
    do_something()
    return render(response, 'app1/home.html')
# Create your views here.
