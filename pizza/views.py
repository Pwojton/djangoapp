from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'pizza/index.html')


def news(request):
    return render(request, 'pizza/news.html')


def gallery(request):
    return HttpResponse("Witaj w galerii")
