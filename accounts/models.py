from django.db import models
from django.contrib.auth.models import AbstractUser

def avatar_upload_to(instance, filename):
    return f"avatars/{instance.username}/{filename}"

class Account(AbstractUser):
    avatar = models.ImageField(
        upload_to=avatar_upload_to,
        default="default/avatar.png",
        blank=True,
        null=True,
        verbose_name="Avatar"
    )
    
    pais = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    dni = models.CharField(max_length=15, unique=True, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"