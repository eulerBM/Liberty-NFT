from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def author(request):
    if request.method == 'GET':
        return render (request, 'author.html')


