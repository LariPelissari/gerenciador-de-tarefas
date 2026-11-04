import pytest
from app.models import TarefaCreate
from app.models import TarefaUpdate
from app.repositories import tarefas as repository
from app.models import TarefaStatusUpdate

@pytest.fixture(autouse=True)
def limpar_tarefas():
    from app.database import SessionLocal
    from app.models import Tarefa

    db = SessionLocal()

    try:
        db.query(Tarefa).delete()
        db.commit()
    finally:
        db.close()

def test_criar_tarefa():
    tarefa = TarefaCreate(
        titulo="Estudar Python",
        descricao="Praticar testes unitários"
    )

    resultado = repository.criar_tarefa(tarefa)

    assert resultado.id == 1
    assert resultado.titulo == "Estudar Python"
    assert resultado.descricao == "Praticar testes unitários"
    assert resultado.concluida is False

def test_listar_tarefas():
    tarefa1 = TarefaCreate(
        titulo="Estudar Python",
        descricao="Praticar funções"
    )

    tarefa2 = TarefaCreate(
        titulo="Estudar FastAPI",
        descricao="Criar uma API"
    )

    repository.criar_tarefa(tarefa1)
    repository.criar_tarefa(tarefa2)

    resultado = repository.listar_tarefas()

    assert len(resultado) == 2
    assert resultado[0].titulo == "Estudar Python"
    assert resultado[1].titulo == "Estudar FastAPI"

def test_buscar_tarefa():
    tarefa = TarefaCreate(
        titulo="Estudar FastAPI",
        descricao="Aprender a criar APIs"
    )

    tarefa_criada = repository.criar_tarefa(tarefa)

    resultado = repository.buscar_tarefa(tarefa_criada.id)

    assert resultado is not None
    assert resultado.id == tarefa_criada.id
    assert resultado.titulo == "Estudar FastAPI"

def test_buscar_tarefa_inexistente():
    resultado = repository.buscar_tarefa(999)

    assert resultado is None

def test_atualizar_tarefa():
    tarefa = TarefaCreate(
        titulo="Estudar Python",
        descricao="Praticar funções"
    )

    tarefa_criada = repository.criar_tarefa(tarefa)

    tarefa_atualizada = TarefaUpdate(
        titulo="Estudar FastAPI",
        descricao="Criar uma API"
    )

    resultado = repository.atualizar_tarefa(
    tarefa_criada.id,
    tarefa_atualizada
    )

    assert resultado.id == tarefa_criada.id
    assert resultado.titulo == "Estudar FastAPI"
    assert resultado.descricao == "Criar uma API"
    assert resultado.concluida is False

def test_atualizar_tarefa_inexistente():
    tarefa_atualizada = TarefaUpdate(
        titulo="Novo título",
        descricao="Nova descrição"
    )

    resultado = repository.atualizar_tarefa(
        999,
        tarefa_atualizada
    )

    assert resultado is None

def test_excluir_tarefa():
    tarefa = TarefaCreate(
        titulo="Estudar Python",
        descricao="Praticar testes"
    )

    tarefa_criada = repository.criar_tarefa(tarefa)

    resultado = repository.excluir_tarefa(tarefa_criada.id)

    assert resultado.id == tarefa_criada.id
    assert resultado.titulo == "Estudar Python"
    assert repository.buscar_tarefa(tarefa_criada.id) is None

def test_excluir_tarefa_inexistente():
    resultado = repository.excluir_tarefa(999)

    assert resultado is None


def test_atualizar_status_tarefa():
    tarefa = TarefaCreate(
        titulo="Estudar Python",
        descricao="Praticar testes"
    )

    tarefa_criada = repository.criar_tarefa(tarefa)

    novo_status = TarefaStatusUpdate(
        concluida=True
    )

    resultado = repository.atualizar_status_tarefa(
        tarefa_criada.id,
        novo_status
    )

    assert resultado.id == tarefa_criada.id
    assert resultado.concluida is True

def test_atualizar_status_tarefa_inexistente():
    novo_status = TarefaStatusUpdate(
        concluida=True
    )

    resultado = repository.atualizar_status_tarefa(
        999,
        novo_status
    )

    assert resultado is None