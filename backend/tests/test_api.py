import pytest

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture(autouse=True)
def limpar_tarefas():
    from main import tarefas

    tarefas.clear()


def test_inicio():
    resposta = client.get("/")

    assert resposta.status_code == 200
    assert resposta.json() == {
        "mensagem": "Bem-vindo à API TaskFlow!"
    }


def test_criar_tarefa():
    resposta = client.post(
        "/tarefas",
        json={
            "titulo": "Estudar pytest",
            "descricao": "Aprender testes automatizados"
        }
    )

    assert resposta.status_code == 200

    dados = resposta.json()

    assert dados["id"] == 1
    assert dados["titulo"] == "Estudar pytest"
    assert dados["descricao"] == "Aprender testes automatizados"
    assert dados["concluida"] is False


def test_listar_tarefas():
    # Primeiro, cadastramos uma tarefa
    client.post(
        "/tarefas",
        json={
            "titulo": "Estudar pytest",
            "descricao": "Testar listagem de tarefas"
        }
    )

    # Depois, solicitamos a lista de tarefas
    resposta = client.get("/tarefas")

    assert resposta.status_code == 200

    dados = resposta.json()

    assert len(dados) == 1
    assert dados[0]["titulo"] == "Estudar pytest"
    assert dados[0]["descricao"] == "Testar listagem de tarefas"

def test_buscar_tarefa():
    # Criamos uma tarefa para consultar
    client.post(
        "/tarefas",
        json={
            "titulo": "Aprender FastAPI",
            "descricao": "Testar busca por ID"
        }
    )

    # Buscamos a tarefa de ID 1
    resposta = client.get("/tarefas/1")

    assert resposta.status_code == 200

    dados = resposta.json()

    assert dados["id"] == 1
    assert dados["titulo"] == "Aprender FastAPI"
    assert dados["descricao"] == "Testar busca por ID"


def test_buscar_tarefa_inexistente():
    resposta = client.get("/tarefas/999")

    assert resposta.status_code == 404

    dados = resposta.json()

    assert dados["detail"] == "Tarefa não encontrada"

def test_atualizar_tarefa():
    # Primeiro, criamos uma tarefa
    client.post(
        "/tarefas",
        json={
            "titulo": "Estudar Python",
            "descricao": "Descrição antiga"
        }
    )

    # Atualizamos a tarefa de ID 1
    resposta = client.put(
        "/tarefas/1",
        json={
            "titulo": "Estudar FastAPI",
            "descricao": "Descrição atualizada"
        }
    )

    assert resposta.status_code == 200

    dados = resposta.json()

    assert dados["id"] == 1
    assert dados["titulo"] == "Estudar FastAPI"
    assert dados["descricao"] == "Descrição atualizada"
    assert dados["concluida"] is False


def test_atualizar_tarefa_inexistente():
    resposta = client.put(
        "/tarefas/999",
        json={
            "titulo": "Tarefa inexistente",
            "descricao": "Não deve ser atualizada"
        }
    )

    assert resposta.status_code == 404
    assert resposta.json()["detail"] == "Tarefa não encontrada"

    resposta = client.put(
        "/tarefas/1",
        json={
            "titulo": "Estudar FastAPI",
            "descricao": "Descrição atualizada"
        }
    )

def test_excluir_tarefa():
    # Criamos uma tarefa
    criacao = client.post(
        "/tarefas",
        json={
            "titulo": "Excluir tarefa",
            "descricao": "Testar exclusão"
        }
    )

    tarefa_id = criacao.json()["id"]

    # Excluímos a tarefa
    resposta = client.delete(f"/tarefas/{tarefa_id}")

    assert resposta.status_code == 200

    dados = resposta.json()

    assert dados["mensagem"] == "Tarefa excluída com sucesso"
    assert dados["tarefa"]["id"] == tarefa_id

    # Verificamos se ela realmente desapareceu
    consulta = client.get(f"/tarefas/{tarefa_id}")

    assert consulta.status_code == 404


def test_excluir_tarefa_inexistente():
    resposta = client.delete("/tarefas/999")

    assert resposta.status_code == 404
    assert resposta.json()["detail"] == "Tarefa não encontrada"