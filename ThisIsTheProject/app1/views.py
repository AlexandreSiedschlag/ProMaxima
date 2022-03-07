from django.http import HttpResponse
from django.shortcuts import redirect, render
from .functions import do_something, getNumberPages
from .forms import WebSiteInfoForm
from .models import *

def home(response):
    info = WebSiteInfo.objects.all()
    totalRegisters = info.count()
    totalPages = getNumberPages()
    context = {'info': info, 'totalRegisters':totalRegisters, 'totalPages':totalPages}
    return render(response, 'app1/home.html', context)

def scrap(response):
    do_something()
    return render(response, 'app/home.html')

def create(response):
    table = WebSiteInfo.objects.all()
    return redirect(response, 'app1/home.html' , table)

def edit(response):
    return render(response, 'app1/data.html')
# Create your views here.
