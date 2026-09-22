from django.db import models


class Propietario(models.Model):
    identificacion = models.CharField(max_length=20, unique=True, blank=False)
    nombre = models.CharField(max_length=100, blank=False)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)
    propietario = models.ForeignKey(
        Propietario, on_delete=models.CASCADE, related_name='mascotas'
    )

    def __str__(self):
        return self.nombre


class ConsultaVeterinaria(models.Model):
    mascota = models.ForeignKey(
        Mascota, on_delete=models.CASCADE, related_name='consultas'
    )
    fecha = models.DateField(auto_now_add=True)
    motivo = models.CharField(max_length=200, blank=False)
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.mascota} - {self.motivo}"