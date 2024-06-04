from django import forms
from .models import *

class NotaForm(forms.ModelForm):
    fecha = models.DateField()
    titulo = models.CharField(max_length = 100)
    contenido = models.TextField()

    class Meta:
        model = Nota
        fields = ['fecha', 'titulo', 'contenido']

    def save(self, commit=True):
        nota = super().save(commit=False)
        if commit:
            nota.save()
        return nota