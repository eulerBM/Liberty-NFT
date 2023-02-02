from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import  redirect
from criar.models import *
from autor.models import *
import requests



@login_required
def author(request):
    if request.method == 'GET':
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
    



