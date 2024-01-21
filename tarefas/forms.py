from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ("titulo", "descricao")
        labels = {
            'titulo': 'Título',
            'descricao': 'Descrição',
        }
