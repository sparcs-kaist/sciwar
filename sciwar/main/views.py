from django.http import HttpResponse
from django.shortcuts import render

def main_page(request):
    return render(request, 'index.html')

def proto(request):
    return render(request, 'main.html')
