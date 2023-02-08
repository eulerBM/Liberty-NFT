from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from criar.models import *

@login_required
def explore(request):
    if request.method == 'GET':
        item_all = items.objects.all()[:5]

        if request.GET.get('keyword'):
            get_search = request.GET.get('keyword')
            item_filter = items.objects.filter(titulo=get_search)
                      
            context = {
                'items_filter': item_filter,
                'items': item_all,
                
            }
            return render (request, 'explore.html', context)
    
        # se o imput for falso mostre isso

        item_all = items.objects.all()
    
        context = {
            'items': item_all,

        }
        return render (request, 'explore.html', context)
    
    

    
    


