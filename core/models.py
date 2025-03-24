from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ROLES = (('ADMIN', 'ADMINISTRADOR'), ('AGENTE', 'AGENTE'), ('CLIENTE', 'CLIENTE'))
    rol = models.CharField(max_length=10, choices=ROLES, default='CLIENTE')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_groups',  # Cambia el related_name para evitar conflictos
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_permissions',  # Cambia el related_name para evitar conflictos
        blank=True
    )

class Propiedad(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to="propiedades/")  # Guardará imágenes en /media/propiedades/
    direccion = models.CharField(max_length=100)
    agente = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 'AGENTE'})

    def __str__(self):
        return self.titulo


