from django.db import models

# Create your models here.
class Nota(models.Model):  
    fecha = models.DateField()
    titulo = models.CharField(max_length = 100)
    contenido = models.TextField()

    def __str__(self):
        return f"La nota fue guardada en: {self.fecha} con el título '{self.titulo}' y el contenido '{self.contenido[:50]}'"