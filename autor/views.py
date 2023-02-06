from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import  redirect
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
def seguir(request, id):
    seguido = User.objects.get(id=id)
    seguidor = request.user
    Seguir.objects.create(seguidor=seguidor, seguido=seguido)
    return HttpResponse('Você seguiu o usuário')

@login_required
def deixar_de_seguir(request, id):
    seguido = User.objects.get(id=id)
    seguidor = request.user
    Seguir.objects.filter(seguidor=seguidor, seguido=seguido).delete()
    return HttpResponse('Você desseguiu o usuário')
    



