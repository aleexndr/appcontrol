from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Alimentos
from fractions import Fraction

from django.db import connection

# Create your views here.




def reiniciar_alimentos(request):
    with connection.cursor() as cursor:
        cursor.execute("TRUNCATE TABLE registro_alimentos RESTART IDENTITY CASCADE;")
    
    messages.success(request, "La tabla de alimentos ha sido reiniciada.")
    return redirect('index')


def index(request):
    return render (request, "index.html")

def registrar_alimentos(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('tipo')
        cantidad = request.POST.get('cantidad')
        costo = request.POST.get('costo')
        valor = request.POST.get('valor')

        try:
            if "/" in cantidad:
                cantidad = float(Fraction(cantidad))
            else:
                cantidad = float(cantidad)
            if cantidad < 0:
                messages.error(request, "La cantidad no debe ser negativa")
                return redirect('index')
        except ValueError:
            messages.error(request, "Cantidad inválida")
            return redirect('index')
        
        try:
            costo = float(costo)
            if costo < 0:
                messages.error(request, "El costo no debe ser negativo")
                return redirect('index')
        except ValueError:
            messages.error(request, "Costo inválido")
            return redirect('index')

        if nombre and tipo and cantidad and costo and valor:
            alimentos = Alimentos(nombre=nombre, tipo=tipo, cantidad=cantidad, costo=costo, valor=valor)
            alimentos.save()
            messages.success(request, "Guardado")
            return redirect('index')
        
    return render(request, 'index.html')