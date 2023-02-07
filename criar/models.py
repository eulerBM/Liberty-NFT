from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager
import datetime

class items(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=19, blank=False)
    descricao = models.CharField(max_length=50, blank=False)
    Preco = models.FloatField(blank=False)
    royalties = models.PositiveIntegerField(blank=False)
    image = models.ImageField(upload_to="image/", null=True, blank=True)
    data_atual = models.DateTimeField()
    objects = UserManager()
    

    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        self.data_atual = datetime.datetime.now() + datetime.timedelta(days=5)
        super().save(*args, **kwargs)
    
    


    

    


