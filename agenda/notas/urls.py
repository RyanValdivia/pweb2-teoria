from django.urls import path
from . import views

urlpatterns = [
    path('crearNota/', views.crear_nota, name='crear_nota'),
    path('', views.lista_notas, name='lista_notas')  
]