from django.http import HttpResponse
from django.shortcuts import render

def webpage1(request):
    return render(request, 'Page1.html')

def webpage2(request):
    return render(request, 'Page2.html')

def webpage3(request):
    return render(request, 'Page3.html')

def webpage4(request):
    return render(request, 'Page4.html')

def webpage5(request):
    return render(request, 'Page5.html')