from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tarefa
from .forms import TarefaForm

class ListaTarefaView(ListView):
    model= Tarefa
    template_name = "lista_tarefas.html"
    context_object_name = "tarefas"
class NovaTarefaView(CreateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = "nova_tarefa.html"
    success_url = reverse_lazy("lista_tarefas")
class EditaTarefa(UpdateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = ("edita_tarefa.html")
    success_url = reverse_lazy("lista_tarefas")
class RemoveTarefa(DeleteView):
    model = Tarefa
    template_name = ("remove_tarefa.html")
    success_url = reverse_lazy("lista_tarefas")