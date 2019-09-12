from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Witaj w barze Pizza!")
    return render(request, 'pizza/index.html')

def news(request):
    return HttpResponse("<h1>Nowości w barze</h1>")


def menu(request):
    return HttpResponse("<h2>Menu</h2>")

