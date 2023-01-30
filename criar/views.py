from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from criar.forms import forms_user
from django.contrib import messages
from django.contrib.messages import constants
from criar.models import items

@login_required
def criar (request): 
    form = forms_user() 

    if request.method == 'GET':
        return render(request, 'create.html', {'form': form})

    if request.method == 'POST':
        form = forms_user(request.POST)
               
        if form.is_valid():
            form.save()      
            messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso.')
            form_clean = forms_user()
            return render(request, 'create.html', {'form': form_clean})    
            
        else:
            messages.add_message(request, constants.ERROR, 'Falha, por favor tente outra vez.')
            return render(request, 'create.html', {'form': form}) 
        
    
    
        

        


        




