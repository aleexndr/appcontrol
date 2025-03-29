from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Alimentos, Transporte, Servicios
# from fractions import Fraction
# from django.db import connection
from datetime import date

# Create your views here.



# def reiniciar_alimentos(request):
#     with connection.cursor() as cursor:
#         cursor.execute("TRUNCATE TABLE registro_alimentos RESTART IDENTITY CASCADE;")
    
#     messages.success(request, "La tabla de alimentos ha sido reiniciada.")
#     return redirect('index')


def index(request):
    return render (request, "index.html")

def registros(request):
    alimentos = Alimentos.objects.all()
    return render (request, "registros.html", {"alimentos": alimentos})

def registrar_alimentos(request):
    if request.method == 'POST':
        preciokg_alimentos = request.POST.get('preciokg')
        producto_alimentos = request.POST.get('producto')
        cantidad_alimentos = request.POST.get('cantidad')
        costo_alimentos = request.POST.get('costo')
        errores_alimentos = []

        if not preciokg_alimentos:
            preciokg_alimentos = 0.0
        else:
            try:
                preciokg_alimentos = float(preciokg_alimentos)
            except ValueError:
                errores_alimentos.append("El precio por kg debe ser un número válido.")

        if not producto_alimentos.strip():
            errores_alimentos.append("El nombre del producto esta vacío.")
        
        try:
            costo_alimentos = float(costo_alimentos)
            if costo_alimentos < 0:
                errores_alimentos.append("El costo es invalido")
        except ValueError:
            errores_alimentos.append("Costo inválido. Debe ser un número")

        if  errores_alimentos:
            for error in errores_alimentos:
                messages.error(request, error)
            return redirect('index')
        
        fecha_alimentos = date.today()
        alimentos = Alimentos(
            preciokg_alimentos=preciokg_alimentos, 
            producto_alimentos=producto_alimentos, 
            cantidad_alimentos=cantidad_alimentos, 
            costo_alimentos=costo_alimentos, 
            fecha_alimentos=fecha_alimentos
        )
        alimentos.save()
        messages.success(request, "Guardado")
        return redirect('index')
        
    return render(request, 'index.html')



def registrar_transporte(request):
    if request.method == 'POST':
        opcion_transporte = request.POST.get('opcion_transporte')
        tipo_transporte = request.POST.get('tipo_transporte')
        cantidad_transporte = request.POST.get('cantidad_transporte')
        costo_transporte = request.POST.get('costo_transporte')
        errores_transporte = []
        
        if not opcion_transporte.strip():
            errores_transporte.append("La opcion de transporte esta vacía")

        try:
            costo_transporte = float(costo_transporte)
            if costo_transporte < 0:
                errores_transporte.append("El costo no debe ser negativo")
        except (ValueError, TypeError):
            errores_transporte.append("Costo inválido")

        if errores_transporte:
            for error in errores_transporte:
                messages.error(request, error)
            return redirect('index')
            
        fecha_transporte = date.today()
        transporte = Transporte(
            opcion_transporte=opcion_transporte, 
            tipo_transporte=tipo_transporte,  
            cantidad_transporte=cantidad_transporte, 
            costo_transporte=costo_transporte, 
            fecha_transporte=fecha_transporte
        )
        transporte.save()
        messages.success(request, "Guardado")
        return redirect('index')
        
    return render(request, 'index.html')



def registrar_servicios(request):
    if request.method == 'POST':
        nombre_servicios = request.POST.get('nombre_servicios')
        tipo_servicios = request.POST.get('tipo_servicios')
        costo_servicios = request.POST.get('costo_servicios')
        errores_servicios = []
        
        if not nombre_servicios.strip():
            errores_servicios.append("El nombre del servicio esta vacío.")

        try:
            costo_servicios = float(costo_servicios)
            if costo_servicios < 0:
                errores_servicios.append("El costo no debe ser negativo")
        except (ValueError, TypeError):
            errores_servicios.append("Costo inválido")

        if errores_servicios:
            for error in errores_servicios:
                messages.error(request, error)
            return redirect('index')

        fecha_servicios = date.today()
        servicios = Servicios(
            nombre_servicios=nombre_servicios,
            tipo_servicios=tipo_servicios,
            costo_servicios=costo_servicios,
            fecha_servicios=fecha_servicios
        )
        servicios.save()
        messages.success(request, "Guardado")
        return redirect('index')
        
    return render(request, 'index.html')