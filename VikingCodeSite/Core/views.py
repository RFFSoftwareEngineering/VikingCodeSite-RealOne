from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    context = {
                
    }
    return render(request, "index.html", context)
