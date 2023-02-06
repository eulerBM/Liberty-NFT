from django.core.exceptions import *
from django import forms
from criar.models import items
from django.contrib.auth import get_user_model

class forms_user (forms.ModelForm):
    class Meta:
        model = items
        fields = ['titulo', 'descricao', 'Preco', 'royalties', 'image','id']

class SignupForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name']

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

    