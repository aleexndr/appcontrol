from django import forms
from .models import Alimentos

class AlimentosForm(forms.ModelForm):
    class Meta:
        model = Alimentos
        fields = ['nombre', 'tipo', 'cantidad', 'costo']
