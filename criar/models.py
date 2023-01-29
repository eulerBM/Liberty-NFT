from django.db import models

class items(models.Model):

    usuario = models.CharField(max_length=20, blank=False)
    titulo = models.CharField(max_length=30, blank=False)
    descricao = models.CharField(max_length=50, blank=False)
    Preco = models.FloatField(blank=False)
    royalties = models.PositiveIntegerField(blank=False)
    image = models.ImageField(upload_to="image/", blank=True)

    def __str__(self):
        text = format(f'{self.usuario} / {self.titulo}')
        return text

    

    


