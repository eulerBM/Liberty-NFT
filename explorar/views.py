from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from criar.models import *

@login_required
def explore(request):
    if request.method == 'GET':
        item_all = items.objects.all()

        context = {
            'items': item_all,

        }
        return render (request, 'explore.html', context)
    
    else: 
        get_search = request.POST.get('keyword')
        item_filter = items.objects.filter(titulo=get_search)

        context = {
            'items': item_filter,

        }
        return render (request, 'explore.html', context)

# Create your views here.
