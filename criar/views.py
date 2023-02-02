from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from criar.forms import forms_user
from django.contrib import messages
from django.contrib.messages import constants
from criar.models import *
from datetime import date
import requests



@login_required
def criar (request): 
    if request.method == 'GET': 
        url = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BRL"
        response = requests.get(url).json()
        return render(request, 'create.html', {'form': forms_user(), 'data': date.today(), 'eth': response["BRL"]})

    else:
        form = forms_user(request.POST, request.FILES)
               
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user    
            order.save()
            messages.add_message(request, constants.SUCCESS, 'Item cadastrado com sucesso.')
            return redirect("create")
            
        else:
            messages.add_message(request, constants.ERROR, f'{form.errors}')
            return render(request, 'create.html', {'form': forms_user()}) 
        



        
    
    
        

        


        




