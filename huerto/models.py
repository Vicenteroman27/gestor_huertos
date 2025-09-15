from django.db import models

class Sector(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Cultivo(models.Model):
    ESTADOS = [
        ('semilla', 'Semilla'),
        ('crecimiento', 'En Crecimiento'),
        ('cosecha', 'Listo para Cosechar'),
    ]

    nombre = models.CharField(max_length=100)
    fecha_siembra = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='semilla')
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name="cultivos")

    def __str__(self):
        return f"{self.nombre} - {self.get_estado_display()}"
