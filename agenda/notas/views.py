from django.shortcuts import render, redirect
from .forms import *
from .models import *

#CREAR NOTA
def crear_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotaForm()
    return render(request, 'notas/crearNota.html', {'form': form})

def lista_notas(request):
    notas = Nota.objects.all()
    return render(request, 'notas/index.html', {'notas': notas})