from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def explore(request):
    if request.method == 'GET':
        return render (request, 'explore.html')

# Create your views here.
