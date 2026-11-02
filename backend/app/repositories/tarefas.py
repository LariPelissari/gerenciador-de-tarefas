# Estrutura temporária para armazenar as tarefas
tarefas = []

def criar_tarefa(tarefa):
    nova_tarefa = {
        "id": max((t["id"] for t in tarefas), default=0) + 1,
        "titulo": tarefa.titulo,
        "descricao": tarefa.descricao,
        "concluida": False
    }

    tarefas.append(nova_tarefa)

    return nova_tarefa

def listar_tarefas():
    return tarefas

def buscar_tarefa(tarefa_id):
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            return tarefa

    return None

def atualizar_tarefa(tarefa_id, tarefa_atualizada):
    for indice, tarefa in enumerate(tarefas):
        if tarefa["id"] == tarefa_id:
            tarefas[indice] = {
                **tarefa,
                **tarefa_atualizada.model_dump()
            }

            return tarefas[indice]

    return None

def excluir_tarefa(tarefa_id):
    for indice, tarefa in enumerate(tarefas):
        if tarefa["id"] == tarefa_id:
            return tarefas.pop(indice)

    return None