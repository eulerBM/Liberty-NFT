from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager


class items(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30, blank=False)
    descricao = models.CharField(max_length=50, blank=False)
    Preco = models.FloatField(blank=False)
    royalties = models.PositiveIntegerField(blank=False)
    image = models.ImageField(upload_to="image/", blank=True)
    objects = UserManager()
    

    def __str__(self):
        text = self.titulo
        return text

    

    


