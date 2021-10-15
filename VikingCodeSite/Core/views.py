from django.shortcuts import render, redirect
from django.contrib import messages
import time


def index(request):
    context = {
                
    }
    return render(request, "index.html", context)

def home(request):
    context = {
        
    }
    time.sleep(1.25)
    return render(request, "home.html", context)
