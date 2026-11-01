from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="TaskFlow API",
    description="API para gerenciamento de tarefas",
    version="1.0.0"
)

# Estrutura temporária para armazenar as tarefas
tarefas = []

# Modelo dos dados recebidos no cadastro
class TarefaCreate(BaseModel):
    titulo: str
    descricao: str | None = None

class TarefaUpdate(BaseModel):
    titulo: str
    descricao: str | None = None

@app.get("/")
def inicio():
    return {
        "mensagem": "Bem-vindo à API TaskFlow!"
    }


@app.post("/tarefas")
def criar_tarefa(tarefa: TarefaCreate):

    nova_tarefa = {
        "id": max((tarefa["id"] for tarefa in tarefas), default=0) + 1,
        "titulo": tarefa.titulo,
        "descricao": tarefa.descricao,
        "concluida": False
    }

    tarefas.append(nova_tarefa)

    return nova_tarefa

@app.get("/tarefas")
def listar_tarefas():
    return tarefas

@app.get("/tarefas/{tarefa_id}")
def buscar_tarefa(tarefa_id: int):

    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            return tarefa

    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada"
    )


@app.put("/tarefas/{tarefa_id}")
def atualizar_tarefa(tarefa_id: int, tarefa_atualizada: TarefaUpdate):

    for i, tarefa in enumerate(tarefas):
        if tarefa["id"] == tarefa_id:
            tarefas[i] = {**tarefa, **tarefa_atualizada.model_dump()}
            return tarefas[i]

    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada"
    )

@app.delete("/tarefas/{tarefa_id}")
def excluir_tarefa(tarefa_id: int):

    for indice, tarefa in enumerate(tarefas):
        if tarefa["id"] == tarefa_id:
            tarefa_removida = tarefas.pop(indice)
            return {
                "mensagem": "Tarefa excluída com sucesso",
                "tarefa": tarefa_removida
            }

    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada"
    )