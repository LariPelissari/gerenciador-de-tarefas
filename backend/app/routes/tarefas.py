from fastapi import APIRouter, HTTPException

from app.models import TarefaCreate, TarefaUpdate

from app.repositories import tarefas as repository

router = APIRouter(
    prefix="/tarefas",
    tags=["Tarefas"]
)


@router.post("/")
def criar_tarefa(tarefa: TarefaCreate):
    return repository.criar_tarefa(tarefa)


@router.get("/")
def listar_tarefas():
    return repository.listar_tarefas()


@router.get("/{tarefa_id}")
def buscar_tarefa(tarefa_id: int):
    tarefa = repository.buscar_tarefa(tarefa_id)

    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    return tarefa


@router.put("/{tarefa_id}")
def atualizar_tarefa(tarefa_id: int, tarefa_atualizada: TarefaUpdate):
    tarefa = repository.atualizar_tarefa(tarefa_id, tarefa_atualizada)

    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    return tarefa


@router.delete("/{tarefa_id}")
def excluir_tarefa(tarefa_id: int):
    tarefa_removida = repository.excluir_tarefa(tarefa_id)

    if tarefa_removida is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    return {
        "mensagem": "Tarefa excluída com sucesso",
        "tarefa": tarefa_removida
    }
