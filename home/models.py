from django.db import models


# Cadastro de item

class items(models.Model):

    titulo: models.CharField(max_length=30, blank=False)
    descricao = models.TextField(max_length=50, blank=False)
    usuario = models.CharField(max_length=20, blank=False)
    Preco = models.BooleanField(blank=False)
    royalties = models.PositiveIntegerField(blank=False)
    image = models.ImageField()

    




# Create your models here.
