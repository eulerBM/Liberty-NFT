from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from criar.models import *

def home(request):
    if request.method == 'GET':
        bd_all = items.objects.all()[:3]
        bd_item = items.objects.all()[:6]

        context = {
            'item':bd_all,
            'item_all':bd_item,
        }
        return render (request, 'index.html', context)


