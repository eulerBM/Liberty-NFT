from django.shortcuts import render

def home(request):
    if request.method == 'GET':
        return render (request, 'index.html')

def explore(request):
    if request.method == 'GET':
        return render (request, 'explore.html')

def details(request):
    if request.method == 'GET':
        return render (request, 'details.html')

def author(request):
    if request.method == 'GET':
        return render (request, 'author.html')

# Create your views here.
