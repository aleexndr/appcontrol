from django.shortcuts import render, redirect
from .models import Alimentos

# Create your views here.

def index(request):
    return render (request, "index.html")

def registrar_alimentos(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('tipo')
        cantidad = request.POST.get('cantidad')
        costo = request.POST.get('costo')

        if nombre and tipo and cantidad and costo:
            alimentos = Alimentos(nombre=nombre, tipo=tipo, cantidad=cantidad, costo=costo)
            alimentos.save()
            return redirect('index')
        
    return render(request, 'index.html')