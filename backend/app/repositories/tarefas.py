from app.database import SessionLocal
from app.models import Tarefa


def criar_tarefa(tarefa):
    db = SessionLocal()

    try:
        nova_tarefa = Tarefa(
            titulo=tarefa.titulo,
            descricao=tarefa.descricao,
            concluida=False
        )

        db.add(nova_tarefa)
        db.commit()
        db.refresh(nova_tarefa)

        return nova_tarefa

    finally:
        db.close()

def listar_tarefas():
    db = SessionLocal()

    try:
        return db.query(Tarefa).all()

    finally:
        db.close()

def buscar_tarefa(tarefa_id):
    db = SessionLocal()

    try:
        return db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()

    finally:
        db.close()

def atualizar_tarefa(tarefa_id, tarefa_atualizada):
    db = SessionLocal()

    try:
        tarefa = db.query(Tarefa).filter(
            Tarefa.id == tarefa_id
        ).first()

        if tarefa is None:
            return None

        tarefa.titulo = tarefa_atualizada.titulo
        tarefa.descricao = tarefa_atualizada.descricao

        db.commit()
        db.refresh(tarefa)

        return tarefa

    finally:
        db.close()

def excluir_tarefa(tarefa_id):
    db = SessionLocal()

    try:
        tarefa = db.query(Tarefa).filter(
            Tarefa.id == tarefa_id
        ).first()

        if tarefa is None:
            return None

        db.delete(tarefa)
        db.commit()

        return tarefa

    finally:
        db.close()

def atualizar_status_tarefa(tarefa_id, novo_status):
    db = SessionLocal()

    try:
        tarefa = db.query(Tarefa).filter(
            Tarefa.id == tarefa_id
        ).first()

        if tarefa is None:
            return None

        tarefa.concluida = novo_status.concluida

        db.commit()
        db.refresh(tarefa)

        return tarefa

    finally:
        db.close()