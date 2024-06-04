from datetime import date
from django import forms
from .models import *

class NotaForm(forms.ModelForm):
    fecha = models.DateField(default=date.today)
    titulo = models.CharField(max_length = 100)
    contenido = models.TextField()

    class Meta:
        model = Nota
        fields = ['fecha', 'titulo', 'contenido']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

    def save(self, commit=True):
        nota = super().save(commit=False)
        if commit:
            nota.save()
        return nota