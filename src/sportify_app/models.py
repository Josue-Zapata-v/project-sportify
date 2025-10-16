from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} ({self.ciudad})"

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=50)
    numero_camiseta = models.PositiveIntegerField()
    equipo = models.ForeignKey(
        Equipo, 
        related_name="jugadores", 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.nombre} - {self.posicion} #{self.numero_camiseta}"
