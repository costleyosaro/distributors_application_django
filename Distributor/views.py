from django.shortcuts import render,redirect
from django.http import HttpResponse

def home(request):
    return render(request, 'Ghadco_PH(1).html')

def about(request):
    return render(request, "Ghadco_PH_About.html")

def redirect_to_home(request):
    return redirect('home')

def help(request):
    return render(request, "Ghadco_ph_help(1).html")