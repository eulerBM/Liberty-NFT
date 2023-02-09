from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import  redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q
from criar.models import *
from .models import *
from .forms import *
import requests



@login_required
def author(request):
    if request.method == 'GET':
        if items.objects.filter(data_atual=datetime.datetime.now()):
            delet_item = items.objects.filter(data_atual=datetime.datetime.now())     
            delet_item.delete()
        items_list = items.objects.filter(user=request.user)
        url = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BRL"
        response = requests.get(url).json()
        eth_price = response["BRL"]
       

        for item in items_list:
            item.total = '{:,.2f}'.format(int(item.Preco * eth_price))
            
        context = {
            'item': items_list,
            'eth': eth_price,        
                      
        }
        

        return render (request, 'author.html', context)
    
    
@login_required
def conta_de_outro_user(request, id):

    if request.method == 'GET':
        get_user = User.objects.get(id=id)
        filter_user = items.objects.filter(user=id)
        contagem_segui = Seguir.objects.filter(seguido=id).__len__
        
        busca = Q(
            Q(seguidor=request.user.id) & Q(seguido=id)
        )

        nao_segue = Seguir.objects.filter(busca)
        
        context = {
            'user': get_user,
            'item': filter_user,
            'contagem': contagem_segui,
            'nao_segue': nao_segue,
            
            
        }

        return render (request, 'author_user.html', context)

        
           
    


@login_required
def seguir(request, user_id):
    seguido = User.objects.get(pk=user_id)
    Seguir.objects.get_or_create(seguidor=request.user, seguido=seguido)
    return redirect('author', user_id=user_id)

@login_required
def deixar_de_seguir(request, user_id):
    seguido = User.objects.get(pk=user_id)
    Seguir.objects.filter(seguidor=request.user, seguido=seguido).delete()
    return redirect('author', user_id=user_id)



