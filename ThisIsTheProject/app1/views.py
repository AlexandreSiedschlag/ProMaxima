from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .functions import do_something, getNumberPages
from .forms import WebSiteInfoForm
from .models import *


def home(request):
    info = WebSiteInfo.objects.all()
    totalRegisters = info.count()
    totalPages = getNumberPages()
    context = {'info': info, 'totalRegisters':totalRegisters, 'totalPages':totalPages}
    return render(request, 'app1/home.html', context)

def scrap(request):
    do_something()
    return redirect(request, 'app/home.html')

def createOrder(request):
    form = WebSiteInfoForm()
    if request.method =='POST':
        # print('Printing POST:', request.POST)
        form = WebSiteInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'app1/create.html', context)

def updateOrder(request, pk):
    table = WebSiteInfo.objects.get(id=pk)
    form = WebSiteInfoForm(instance=table)
    if request.method =='POST':
        # print('Printing POST:', request.POST)
        form = WebSiteInfoForm(request.POST, instance=table)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'app1/update.html', context)

def deleteOrder(request, pk):
    table = WebSiteInfo.objects.get(id=pk)
    context = {'item':table}
    return render(request, 'app1/delete.html', context)

