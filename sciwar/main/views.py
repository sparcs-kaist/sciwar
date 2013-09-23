from django.http import HttpResponse
from django.shortcuts import render

def proto(request):
    return render(request, 'main.html')
