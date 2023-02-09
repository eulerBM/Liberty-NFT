from django.db import models
from django.contrib.auth.models import User


class Seguir(models.Model):
    seguidor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seguidor')
    seguido = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seguido')

    def __str__(self):
        return f'{self.seguidor} segue {self.seguido}'
  

