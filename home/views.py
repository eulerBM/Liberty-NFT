from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    if request.method == 'GET':
        return render (request, 'index.html')
@login_required
def explore(request):
    if request.method == 'GET':
        return render (request, 'explore.html')
@login_required
def details(request):
    if request.method == 'GET':
        return render (request, 'details.html')


# Create your views here.
