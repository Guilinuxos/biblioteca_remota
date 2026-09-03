from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length = 200)
    autor = models.CharField(max_length = 200)
    sinopse = models.CharField(blank=True)
    editora = models.CharField(max_length = 200)
    genero = models.CharField(max_length= 100)
    ano = models.PositiveIntegerField(
        validators = [MinValueValidator(1000), MaxValueValidator(9999)]
    )
    capa = models.ImageField(upload_to="capas/")
    def __str__(self):
        return self.titulo

