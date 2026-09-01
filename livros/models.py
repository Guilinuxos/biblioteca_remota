from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length = 200)
    autor = models.CharField(max_length = 200)
    editora = models.CharField(max_length = 200)
    ano = models.PositiveIntegerField(
        validators = [MinValueValidator(1000), MaxValueValidator(9999)]
    )
    capa = models.ImageField(upload_to="capas/")