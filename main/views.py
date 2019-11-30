from django.shortcuts import render

from main.tasks import boyC, girlC, infinityC
# Create your views here.

def index(request):
    return render(request, 'index.html')

def boy(request):
    boyC.delay()
    return render(request, 'index.html')

def girl(request):
    girlC.delay()
    return render(request, 'index.html')

def infinity(request):
    infinityC.delay()
    return render(request, 'index.html')
