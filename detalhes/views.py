from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def details(request):
    if request.method == 'GET':
        return render (request, 'details.html')
