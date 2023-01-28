from django.shortcuts import render, redirect,HttpResponse
from criar.forms import forms_user

def criar(request):
    form = forms_user()

    if request.method == 'GET':
        return render (request, 'create.html', {'form':form})


    if request.method == 'POST':
        form = forms_user(request.POST)

        if request.POST:
            if form.is_valid():
                form.save()
                return redirect ('create')
                    
        return render (request, 'create.html', {'form':form})

    



        

    


# Create your views here.
