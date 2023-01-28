from django.core.exceptions import *
from django import forms
from criar.models import items


class forms_user (forms.ModelForm):
    class Meta:
        model = items
        fields = '__all__'

    