from django.shortcuts import render

from main.tasks import boyC, girlC, infinityC, p1, p2, p3, p4
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

def p11(request,t):
    p1.delay(t)
    return render(request, 'index.html')

def p22(request):
    p2.delay()
    return render(request, 'index.html')

def p33(request):
    p3.delay()
    return render(request, 'index.html')

def p44(request):
    p4.delay()
    return render(request, 'index.html')