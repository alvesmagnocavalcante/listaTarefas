from django.urls import path
from .views import ListaTarefaView, EditaTarefa, NovaTarefaView, RemoveTarefa

urlpatterns = [
    path('', ListaTarefaView.as_view(), name='lista_tarefas'),
    path('nova/', NovaTarefaView.as_view(), name='nova_tarefa'),
    path('edita/int:<pk>', EditaTarefa.as_view(), name='edita_tarefa'),
    path('remove/int:<pk>', RemoveTarefa.as_view(), name='remove_tarefa')
]