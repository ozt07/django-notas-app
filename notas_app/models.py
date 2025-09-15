from django.db import models
from django.contrib.auth.models import User

class Calculo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    expresion = models.CharField(max_length=255)
    resultado = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.expresion} = {self.resultado}"
    
    class Meta:
        verbose_name = "Cálculo"
        verbose_name_plural = "Cálculos"
        ordering = ['-fecha_creacion']