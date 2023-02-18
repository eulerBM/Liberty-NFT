from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from criar.models import *
from autor.models import *

def home(request):
    if request.method == 'GET':
        bd_all = items.objects.all()[:3]
        bd_item = items.objects.all()[:6]

        try:
            saldo = Saldo.objects.get(user=request.user).saldo

        except Saldo.DoesNotExist:
            saldo = '0'

        context = {
            'item':bd_all,
            'item_all':bd_item,
            'saldo': saldo
        }
        return render (request, 'index.html', context)


