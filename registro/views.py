from django.shortcuts import render, redirect
from .forms import AlimentosForm

# Create your views here.

def index(request):
    return render (request, "index.html")

def registrar_alimentos(request):
    if request.method == 'POST':
        form = AlimentosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlimentosForm()
    
    return render(request, 'index.html', {'form': form})