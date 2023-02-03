from django.db import models
from django.contrib.auth.models import User


class Seguir(models.Model):
    seguidor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seguindo')
    seguido = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seguidores')

    def __str__(self):
        return f'{self.seguidor} segue {self.seguido}'
  


