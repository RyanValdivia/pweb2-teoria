from django import forms
from .models import *

class NotaForm(forms.ModelForm):
    fecha = models.DateField()
    titulo = models.CharField(max_length = 100)
    contenido = models.TextField()

    class Meta:
        model = Notas
        fields = ['fecha', 'titulo', 'contenido']

