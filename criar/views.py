from django.shortcuts import render, redirect
from criar.forms import forms_user
from django.contrib import messages
from django.contrib.messages import constants
from criar.models import items


def criar (request): 
    form = forms_user() 

    if request.method == 'GET':
        return render(request, 'create.html', {'form': form})

    if request.method == 'POST':
        form = forms_user(request.POST)
        get_username = request.POST.get('usuario')
        get_user_bd = items.objects.filter(usuario=get_username)
        
        if get_user_bd:
            messages.add_message(request, constants.ERROR, 'Usuario ja existe, tente outro.')
            return render(request, 'create.html', {'form': form}) 
       
        elif form.is_valid():
            form.save()
            get_user = items.objects.get(usuario=get_username)
            messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso.')
            return render(request, 'create.html', {'form': form, 'usuario': get_user})    
            
        else:
            messages.add_message(request, constants.ERROR, 'Falha, por favor tente outra vez.')
            return render(request, 'create.html', {'form': form}) 
        
    
    
        

        


        




