from django.shortcuts import render
from criar.models import *
from django.contrib.auth.decorators import login_required
import requests


@login_required
def details(request, id):
    if request.method == 'GET':
        item = items.objects.get(id=id)
        url = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BRL"
        response = requests.get(url).json()
        eth_price = response["BRL"]
        resul = '{:,.2f}'.format(int(item.Preco * eth_price))
        item_all = items.objects.all()[:6]  

        

        context = {
            'item': item,
            'eth': resul,
            'item_2': item_all
            

        }


        return render (request, 'details.html', context)